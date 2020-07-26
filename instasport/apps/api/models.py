from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Workout(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client')
    coach = models.ForeignKey(User, on_delete=models.CASCADE, related_name='coach')
    name = models.CharField(max_length=100, default='Workout')
    date = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.name