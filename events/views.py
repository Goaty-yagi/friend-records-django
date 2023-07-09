from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import JsonResponse

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import EventCreateSerializer
from .models import Event
from friends.models import Friend
from rest_framework_simplejwt.authentication import JWTAuthentication

# class OwnerOnlyRestriction(UserPassesTestMixin):
#     '''
#     restriction of owner user can access the only event data
#     '''
#     def test_func(self):
#         print('in_testfun',self.request.__dir__())
#         owner_user = self.request.user
#         object_user = Friend.objects.get(id=self.get_object().friend_id).user
#         print("owner",owner_user, "object",object_user)
#         verification = True if owner_user.is_staff or owner_user==object_user else False
#         return verification
    
#     def handle_no_permission(self):
#         return JsonResponse({"info":"not allowed"},status=403)

class EventCreateApi(generics.CreateAPIView):
    serializer_class = EventCreateSerializer
    queryset = Event.objects.all()


class EventListApi(generics.ListAPIView):
    serializer_class = EventCreateSerializer
    queryset = Event.objects.all()


class EventUserListApi(APIView):
    # get characterevent list.
    def post(self, request):
        friend_id = request.data.pop('friend')
        friend_event = Event.objects.filter(friend=friend_id)
        serializer = EventCreateSerializer(friend_event, many=True)
        return Response(serializer.data)


class EventDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventCreateSerializer
    queryset = Event.objects.all()
    lookup_field = 'id'

    def perform_update(self, serializer):
        pre_instance = self.get_object()  # instance before update
        instance = serializer.save()
        diff_money = instance.money - pre_instance.money
        friend = Friend.objects.get(id=instance.friend.id)
        friend.sum += diff_money
        friend.save()

    def perform_destroy(self, instance):
        friend = Friend.objects.get(id=instance.friend.id)
        friend.sum -= instance.money
        instance.delete()
        friend.save()  