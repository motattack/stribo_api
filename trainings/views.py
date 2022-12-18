from rest_framework import viewsets

from trainings.models import Training
from trainings.serizalizers import TrainingSerializer


class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer