from django.urls import path
from rest_framework.routers import DefaultRouter

from trainings.views import TrainingViewSet, TrainingExpViewSet

router = DefaultRouter()
router.register(r'', TrainingViewSet, basename='trainings')

urlpatterns = [
                  path('<int:pk>/exp/', TrainingExpViewSet.as_view({'get': 'retrieve'})),
              ] + router.urls
