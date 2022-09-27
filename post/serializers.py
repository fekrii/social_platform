from rest_framework import serializers
from _auth.serializers import CustomUserSerializer
from post.models import BasePost, TravelPost, NewsPost, EventPost


class TravelPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelPost
        fields = [
            'content',
            'destinationCountry'
        ]


class NewsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPost
        fields = [
            'content',
            'link'
        ]


class EventPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventPost
        fields = [
            'eventName',
            'eventStartTime',
            'eventLocation'
        ]


class BasePostSerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(read_only=True)
    travelpost = TravelPostSerializer(read_only=True)
    newspost = TravelPostSerializer(read_only=True)
    eventpost = TravelPostSerializer(read_only=True)


    class Meta:
        model = BasePost
        fields = [
            'id',
            'title',
            'timestamp',
            'created_by',
            'travelpost',
            'newspost',
            'eventpost',
            'views_count'

        ]

