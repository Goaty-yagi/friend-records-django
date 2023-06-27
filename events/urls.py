from django.urls import path, include
from .views import EventCreateApi, EventListApi, EventDetailApi, EventUserListApi

urlpatterns = [
  path('event-create/', EventCreateApi.as_view()),
  path('event-list/', EventListApi.as_view()),
  path('event-userlist/', EventUserListApi.as_view()),
  path('event-detail/<id>', EventDetailApi.as_view()),
]