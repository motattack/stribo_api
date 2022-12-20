from django.contrib import admin

from trainings.models import Training, Exercise, TrainingExercise

# Register your models here.
admin.site.register(Training)
admin.site.register(Exercise)
admin.site.register(TrainingExercise)


