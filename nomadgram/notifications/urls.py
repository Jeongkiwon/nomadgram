from django.urls import path
from . import views
#check
app_name = "notifications"
urlpatterns = [
    path(
        "", view=views.Notifications.as_view(),name="notifications"
    ),
    
]
