from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Notifications)
class NotificationAdmin(admin.ModelAdmin):
    list_display=(
        'creator',
        'to',
        'notification_type'
    )