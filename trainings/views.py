from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from trainings.models import Training
from trainings.serizalizers import TrainingSerializer


class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer


class TrainingExpViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        token = request.headers.get('auth')
        print(token)

        training = self.get_object()
        training.change_experience(request.user)
        return Response({'status': 'ok'})