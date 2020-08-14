from rest_framework import serializers

from account.models import User
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='user_name', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='user_name', queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']
