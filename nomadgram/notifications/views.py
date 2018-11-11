from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
# Create your views here.

class Notifications(APIView):
    def get(self,request, format=None):
        user=request.user

        notifications=models.Notifications.objects.filter(to=user)
        serializer=serializers.NotificationSerializer(notifications, many=True)

        return Response(data=serializer.data, status=200)


def create_notification(creator, to, notification_type, image=None, comment=None):
    notification=models.Notifications.objects.create(
        creator=creator,
        to=to,
        notification_type=notification_type,
        image=image,
        comment=comment,
    )
    notification.save