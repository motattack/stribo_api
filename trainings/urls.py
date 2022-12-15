from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import TrainingsViewSet, testView

r = DefaultRouter()
r.register('trainings', TrainingsViewSet)

urlpatterns = [
    path('test/', testView.as_view()),
] + r.urls
