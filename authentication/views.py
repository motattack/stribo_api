from django.contrib.auth import authenticate
from django.db import IntegrityError
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ParseError
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from authentication.models import User

from authentication.serializers import UserSerializer


class RegisterView(APIView):
    @staticmethod
    def post(request):
        try:
            data = JSONParser().parse(request)
        except ParseError:
            return JsonResponse({'error': 'Bad request'},
                                status=400)

        if not data.get('email') or not data.get('password'):
            return JsonResponse({'error': 'E-mail или пароль не заполнены'},
                                status=400)

        try:
            user = User.objects.create_user(data.get('email'), data.get('password'))
            token = Token.objects.create(user=user)
            return JsonResponse({'success': 'Пользователь успешно зарегистрирован',
                                 'token': token.key,
                                 'user': UserSerializer(user).data},
                                status=201)
        except IntegrityError:
            return JsonResponse({'error': 'Пользователь с таким E-mail уже существует'},
                                status=400)


class LoginView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        user = authenticate(email=data['email'],
                            password=data['password'])
        if user:
            return JsonResponse({'status': 'ok',
                                 'token': user.auth_token.key,
                                 'user': UserSerializer(user).data},
                                status=200)
        else:
            return JsonResponse({'status': 'error',
                                 'message': 'Неверный email или пароль'},
                                status=400)


class TokenView(APIView):
    @staticmethod
    def post(request):
        token = request.data.get('token')
        if Token.objects.filter(key=token).exists():
            return JsonResponse({'status': 'ok',
                                 'user': UserSerializer(Token.objects.get(key=token).user).data},
                                status=200)
        else:
            return JsonResponse({'status': 'error',
                                 'message': 'Неверный токен'},
                                status=400)
