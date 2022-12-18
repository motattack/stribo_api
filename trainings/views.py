from django.shortcuts import render
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.parsers import JSONParser

from rest_framework.views import APIView

from .models import Training
from .serizalizers import TrainingSerializer


class TrainingsViewSet(ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'description']


class testView(APIView):
    def get(self, request):
        # html code
        return render(request, 'index.html')

    def post(self, request):
        # return json response with data from request
        return Response(request.data)
