from rest_framework import serializers
from .models import Training


class TrainingSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=2)
    time = serializers.SerializerMethodField()
    exp = serializers.SerializerMethodField()
    list_of_exercises = serializers.SerializerMethodField('get_list_of_exercises')

    class Meta:
        model = Training
        fields = ('id', 'name', 'description', 'time', 'image', 'exp', 'list_of_exercises')

    def get_time(self, obj):
        return obj.count_time()

    def get_exp(self, obj):
        return obj.count_exp()

    def get_list_of_exercises(self, obj):
        return obj.list_of_exercises.all().values('name', 'description', 'time', 'exp')

