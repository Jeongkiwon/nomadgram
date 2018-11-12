from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'file',
        'location',
        'creator',
        'caption',
        'created_at',
        'updated_at',
    )

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'creator',
        'image',
        'created_at',
        'updated_at',
    )

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'message',
        'creator',
        'image',
        'created_at',
        'updated_at',
    )