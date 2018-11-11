from rest_framework import serializers
from . import models
from nomadgram.users import serializers as user_serializers
from nomadgram.images import serializers as image_serializers
class NotificationSerializer(serializers.ModelSerializer):

    creator=user_serializers.ListUserSerializer()
    image=image_serializers.SmallImagesSerializer()
    class Meta:
        model=models.Notifications
        fields="__all__"