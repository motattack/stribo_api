from django.db import models
from django.contrib.auth import get_user_model


class Training(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название тренировки')
    description = models.TextField("Описание тренировки", blank=True, null=True)
    list_of_exercises = models.ManyToManyField('Exercise', through='TrainingExercise')
    image = models.ImageField(upload_to='trainings', blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return self.name

    def count_time(self):
        return sum([ex.time for ex in self.list_of_exercises.all()])

    def count_exp(self):
        return sum([ex.exp for ex in self.list_of_exercises.all()])

    def change_experience(self, user):
        user = get_user_model().objects.get(id=user.id)
        user.recalculate_experience(self.count_exp())
        user.save()


class Exercise(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField("Описание упражнения", blank=True, null=True)
    time = models.IntegerField(verbose_name='Время выполнения', blank=True, null=True)
    exp = models.IntegerField(verbose_name='Опыт', blank=True, null=True)

    def __str__(self):
        return self.name


class TrainingExercise(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    order = models.IntegerField()

    def __str__(self):
        return f'{self.training} - {self.exercise}'
