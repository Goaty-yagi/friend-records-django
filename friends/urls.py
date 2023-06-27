from django.urls import path, include
from .views import FriendCreateApi, FriendListApi, FriendDetailApi, UserFriendListApi, FriendBirthdayUpdateApi

urlpatterns = [
    path('friend-create/', FriendCreateApi.as_view()),
    path('friend-list/', FriendListApi.as_view()),
    path('user-friend/', UserFriendListApi.as_view()),
    path('friend-detail/<id>', FriendDetailApi.as_view()),
    path('birthday-update/', FriendBirthdayUpdateApi.as_view()),
]
