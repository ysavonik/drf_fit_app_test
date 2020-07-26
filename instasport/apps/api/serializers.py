from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Workout


class WorkoutSerializer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(many=False, read_only=True,
                                          slug_field='username')
    coach = serializers.SlugRelatedField(many=False, read_only=True,
                                          slug_field='username')

    class Meta:
        model = Workout
        fields = ['client', 'coach', 'name', 'date']