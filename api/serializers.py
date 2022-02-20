from rest_framework import serializers
from . import models

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = ['id', 'name']
        
class TaskTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TaskType
        fields = ['id', 'name']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = ['id', 'task_type', 'person', 'priority_order', 'name', 'description']