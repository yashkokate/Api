

from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class ClientSerializer(serializers.ModelSerializer):  # create class to serializer model

    class Meta:
        model = Client
        fields ="__all__"


class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model

    class Meta:
        model = User
        fields = ('id', 'username','password')

class ProjectSerializer(serializers.ModelSerializer):
    user=UserSerializer
    class Meta:
        model=Project
        fields = ('id', 'username','password')
