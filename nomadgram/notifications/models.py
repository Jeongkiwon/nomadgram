from django.db import models
from nomadgram.users import models as user_models
from nomadgram.images import models as image_models
# Create your models here.
class Notifications(image_models.TimeStampedModel):

    TYPE_CHOICES=(
        ('like','Like'),
        ('comment','Comment'),
        ('follow','Follow')
    )
    creator = models.ForeignKey(user_models.User, related_name='creator',on_delete=models.CASCADE)
    to = models.ForeignKey(user_models.User, related_name='to', on_delete=models.CASCADE)
    notification_type=models.CharField(max_length=20, choices=TYPE_CHOICES)

    image=models.ForeignKey(image_models.Image, on_delete=models.CASCADE, null=True,blank=True)
    comment=models.TextField(null=True,blank=True)