from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.db import models

class User(AbstractUser):
    """ User Model """
    #If you curiouse about AbstractUser`s field plz ctrl+click 
    # First Name and Last Name do not cover name patterns
    # around the globe.

    GENDER_CHOICES =(
        ('male','Male'),
        ('female','Female'),
        ('not-specified','Not specified'),
    )

    profile_image=models.ImageField(null=True)
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    website =models.URLField(_(""), max_length=200, null=True)
    bio = models.TextField(_("Bio of User"), null=True)
    phone = models.CharField(_("Phone of User"), max_length=140, null=True)
    gender = models.CharField(_("Gender of User"), max_length=80, choices=GENDER_CHOICES, null=True)
    followers =models.ManyToManyField("self",blank=True)
    following =models.ManyToManyField("self",blank=True)

    def __str__(self):
        return self.username
    

    @property
    def post_count(self):
        return self.images.all().count()
    
    @property
    def followers_count(self):
        return self.followers.all().count()
    @property
    def following_count(self):
        return self.following.all().count()