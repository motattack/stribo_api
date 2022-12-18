from django.urls import path
from rest_framework.routers import DefaultRouter

from trainings.views import TrainingViewSet

router = DefaultRouter()
router.register(r'', TrainingViewSet, basename='trainings')

urlpatterns = [
              ] + router.urls
