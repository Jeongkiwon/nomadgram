from django.db import models
from taggit.managers import TaggableManager
from nomadgram.users import models as user_models
#if we import many models we make nickname using 'as~' 

# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract=True

class Image(TimeStampedModel):
    """ Image Model """
    file = models.ImageField()
    creator = models.ForeignKey(user_models.User, null=True,on_delete=models.CASCADE, related_name='images')
    location = models.CharField(max_length=140)
    caption = models.TextField()
    tags=TaggableManager()

    @property
    def like_count(self):
        return self.likes.all().count()
    @property
    def comment_count(self):
        return self.comments.all().count()

    def __str__(self):
        return '{} - {}'.format(self.location, self.caption)

class Comment(TimeStampedModel):
    """ Comment Model """
    message= models.TextField()
    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.CASCADE,related_name='comments')
    image =models.ForeignKey(Image, on_delete=models.CASCADE, null=True, related_name='comments') 

    def __str__(self):
        return 'Image Caption: {}- User: {} - Comment: {} '.format( self.image.caption, self.creator.username, self.message)
class Like(TimeStampedModel):
    """ Like Model """
    creator = models.ForeignKey(user_models.User, null=True,on_delete=models.CASCADE, related_name='likes')
    image =models.ForeignKey(Image, on_delete=models.CASCADE, null=True, related_name='likes')
    def __str__(self):
        return 'User: {} - Image Caption: {}'.format(self.creator.username, self.image.caption)