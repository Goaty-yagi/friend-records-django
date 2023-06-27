from rest_framework import serializers
from .models import Friend
from events.serializers import EventCreateSerializer
from events.models import Event

class FriendSerializer(serializers.ModelSerializer):
	event = EventCreateSerializer(many=True, required=False, allow_null=True)
	event_length = serializers.SerializerMethodField('get_eventLengthe')
	class Meta:
		model = Friend
		fields = [
			"id",
			"name",
			"user",
			"sum",
			"birthday",
			"thumbnail",
			"avatar",
			"last_log",
			"created_on",
			"event",
			"event_length",
		]
	def get_eventLengthe(self, instance):
		count = Event.objects.filter(friend=instance.id)
		return len(count)

class FriendCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Friend
		fields = [
			"id",
			"name",
			"user",
			"sum",
			"thumbnail",
			"avatar",
			"last_log",
			"created_on",

		]