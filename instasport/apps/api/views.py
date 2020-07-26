from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api import serializers
from .models import Workout


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = serializers.WorkoutSerializer