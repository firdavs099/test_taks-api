from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Task


class TaskSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
