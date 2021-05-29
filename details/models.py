from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    goal = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Exercises(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Schedule(models.Model):
        created = models.DateTimeField(auto_now_add=True)
        time_rest = models.CharField(max_length=10, default=10)
        exc_time = models.CharField(max_length=10, default=60)
        User = models.ForeignKey(User, on_delete=models.CASCADE)
        exerciselist = models.ManyToManyField(Exercises)

        class Meta:
            ordering = ['created']
