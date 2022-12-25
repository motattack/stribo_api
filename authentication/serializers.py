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

        if validated_data.get('password', None):
            instance.set_password(validated_data['password'])

        instance.save()
        return instance


class UserRankingSerializer(serializers.ModelSerializer):
    total_time = SerializerMethodField('get_total_time')
    name = SerializerMethodField('get_name')

    class Meta:
        model = User
        fields = ('name', 'level', 'exp', 'needExpToNextLevel', 'total_time')

    def get_total_time(self, obj):
        return obj.total_days()

    def get_name(self, obj):
        if obj.name == '' or obj.name is None:
            return 'Аноним'
        else:
            return obj.name


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
