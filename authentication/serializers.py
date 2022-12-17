from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.fields import SerializerMethodField

from .models import User


class UserSerializer(serializers.ModelSerializer):
    token = SerializerMethodField()

    class Meta:
        model = User
        fields = ('name', 'email', 'last_login', 'token', 'level', 'exp', 'needExpToNextLevel')

    def get_token(self, obj):
        return Token.objects.get(user=obj).key
