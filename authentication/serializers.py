from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.fields import SerializerMethodField

from .models import User


class UserSerializer(serializers.ModelSerializer):
    auth_token = SerializerMethodField('get_auth_token')

    class Meta:
        model = User
        fields = ('auth_token', 'name', 'email', 'level', 'exp', 'needExpToNextLevel', 'last_login', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def get_auth_token(self, obj):
        return Token.objects.get(user=obj).key

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
