from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("explore", view=views.ExploreUsers.as_view(), name="explore_uesrs"),
    path("<int:user_id>/follow/", view=views.FollowUser.as_view(),name="follow_user"),
    path("<int:user_id>/unfollow/", view=views.UnFollowUser.as_view(),name="unfollow_user"),
    
    path("<username>/followers/",view=views.UserFollowers.as_view(),name="user_followers"),
    path("<username>/following/",view=views.UserFollowing.as_view(),name="user_following"),
    path("search/",view=views.Search.as_view(),name="search"),
    path("<username>",view=views.UserProfile.as_view(),name="user_profile"),
]
