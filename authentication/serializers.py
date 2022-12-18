from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.fields import SerializerMethodField

from .models import User


class UserSerializer(serializers.ModelSerializer):
    auth_token = SerializerMethodField('get_auth_token')

    class Meta:
        model = User
        fields = ('auth_token', 'name', 'email', 'level', 'exp', 'needExpToNextLevel', 'last_login', 'password')

    def get_auth_token(self, obj):
        return Token.objects.get(user=obj).key

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.level = validated_data.get('level', instance.level)
        instance.exp = validated_data.get('exp', instance.exp)
        instance.needExpToNextLevel = validated_data.get('needExpToNextLevel', instance.needExpToNextLevel)
        instance.last_login = validated_data.get('last_login', instance.last_login)
        instance.set_password(validated_data.get('password', instance.password))
        instance.save()
        return instance


class UserRankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'level')


class ExpSerializer(serializers.Serializer):
    exp = serializers.IntegerField()

    class Meta:
        model = User
        fields = ('exp',)

    def create(self, validated_data):
        return validated_data

    def update(self, instance, validated_data):
        instance.exp = validated_data.get('exp', instance.exp)
        return instance
