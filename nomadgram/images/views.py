from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
from nomadgram.notifications import views as notification_views

class Feed(APIView):
    def get(self, request, format=None):
        user = request.user
        following_users = user.following.all()

        image_list=[]

        for following_user in following_users:
            user_images = following_user.images.all()[:2]

            for image in user_images:
                image_list.append(image)

        sorted_list = sorted(image_list, key=lambda image:image.created_at, reverse=True)

        

        serializer = serializers.ImageSerializer(sorted_list,many=True)

        return Response(serializer.data)


class LikeImage(APIView):
    def post(self, request, image_id, format=None):

        user= request.user

        try:
            found_image = models.Image.objects.get(id= image_id)
        except models.Image.DoesNotExist:
            return Response(status=404)

        try:
            preexisiting_like = models.Like.objects.get(creator=user, image=found_image)
            return Response(status=304)
            
        except models.Like.DoesNotExist:
            new_like = models.Like.objects.create(creator=user, image=found_image)
            new_like.save()

            return Response(status=201)

        notification_views.create_notification(user,found_image.creator,'like',found_image,None)
        return Response(status=200)

class UnLikeImage(APIView):
    def delete(self,request,image_id,format=None):
        
        user= request.user

        try:
            found_image = models.Image.objects.get(id= image_id)
        except models.Image.DoesNotExist:
            return Response(status=404)

        try:
            preexisiting_like = models.Like.objects.get(creator=user, image=found_image)
            preexisiting_like.delete()
            return Response(status=204)
            
        except models.Like.DoesNotExist:
            return Response(status=304)
class CommentOnImage(APIView):
    def post(self, request, image_id, format=None):
        user=request.user
        try:
            found_image = models.Image.objects.get(id= image_id)
        except models.Image.DoesNotExist:
            return Response(status=404)

        serializer = serializers.CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(creator=user, image=found_image)
            notification_views.create_notification(user,found_image.creator,'comment',found_image,serializer.data['message'])
            return Response(data=serializer.data, status=200)
        else:
            return Response(data=serializer.errors, status=404)
       

class Comment(APIView):
    def delete(self,request,comment_id,format=None):
        try:
            user=request.user
            comment=models.Comment.objects.get(id=comment_id, creator=user)
            comment.delete()
            return Response(status=200)
        except models.Comment.DoesNotExist:
            return Response(status=404)

class Search(APIView):
    def get(self, request, format=None):
        hashtags= request.query_params.get('hashtags',None)

        if hashtags is not None:
            hashtags=hashtags.split(",")
            images=models.Image.objects.filter(tags__name__in=hashtags).distinct()

            serializer = serializers.CountImagesSerializer(images,many=True)

            return Response(data=serializer.data, status=200)
        else:
            return Response(status=400)