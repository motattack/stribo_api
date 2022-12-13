from django.contrib.auth import login
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.exceptions import ParseError
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token

from authentication.models import User


# Create your views here.
@api_view(['POST'])
def register_view(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(email=data['email'], password=data['password'])
            user.save()
            token = Token.objects.create(user=user)

            return JsonResponse({'status': 'ok', 'token': token.key}, status=201)
        except IntegrityError:
            return JsonResponse({'status': 'error', 'message': 'Пользователь с таким email уже существует'}, status=400)
        except ParseError:
            return JsonResponse({'status': 'error', 'message': 'Неверный формат данных'}, status=400)
        except KeyError:
            return JsonResponse({'status': 'error', 'message': 'Неверный формат данных'}, status=400)


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.get(email=data['email'])
            if user.check_password(data['password']):
                token = Token.objects.get(user=user)
                return JsonResponse({'status': 'ok', 'login by': user.email}, status=201)
            else:
                return JsonResponse({'status': 'error', 'message': 'Неверный пароль'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Пользователь не найден'}, status=400)
        except ParseError:
            return JsonResponse({'status': 'error', 'message': 'Неверный формат данных'}, status=400)
        except KeyError:
            return JsonResponse({'status': 'error', 'message': 'Неверный формат данных'}, status=400)


@csrf_exempt
def token_view(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            token = Token.objects.get(key=data['token'])
            return JsonResponse({'status': 'ok', 'login by': token.user.email}, status=201)
        except Token.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Неверный токен'}, status=400)
        except ParseError:
            return JsonResponse({'status': 'error', 'message': 'Неверный формат данных'}, status=400)
        except KeyError:
            return JsonResponse({'status': 'error', 'message': 'Неверный формат данных'}, status=400)
