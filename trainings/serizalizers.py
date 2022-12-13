from rest_framework import serializers
from .models import Training


class TrainingSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=2)

    class Meta:
        model = Training
        fields = '__all__'
