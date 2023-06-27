from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from .serializers import FriendCreateSerializer, FriendSerializer
from .models import Friend
import datetime

class FriendCreateApi(generics.CreateAPIView):
    serializer_class = FriendSerializer
    queryset = Friend.objects.all()


class FriendListApi(generics.ListAPIView):
    serializer_class = FriendSerializer
    queryset = Friend.objects.all()


class UserFriendListApi(APIView):
    def post(self, request):
        user = request.user
        friend_list = Friend.objects.filter(user=user)
        serializer = FriendSerializer(friend_list, many=True)
        return Response(serializer.data)

        
class FriendDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FriendSerializer
    queryset = Friend.objects.all()
    lookup_field = 'id'


class FriendBirthdayUpdateApi(APIView):
    def post(self, request):
        year = request.data.pop('year')
        month = request.data.pop('month')
        day = request.data.pop('day')
        friend_id = request.data.pop('id')
        friend = Friend.objects.get(id=friend_id)
        friend.birthday = datetime.date(year, month, day)
        friend.save()
        serializer = FriendSerializer(friend)
        return Response(serializer.data)