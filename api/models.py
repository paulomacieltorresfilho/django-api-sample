from django.db import models
from uuid import uuid4

# Create your models here.

class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=120, unique=True, verbose_name="Nome completo")

class TaskType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    name = models.CharField(max_length=120, unique=True, verbose_name="Nome") 

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    
    # Foreign Keys
    task_type = models.ForeignKey(TaskType, models.CASCADE)
    person = models.ForeignKey(Person, models.CASCADE)
    
    priority_order = models.IntegerField(verbose_name="Prioridade")
    name = models.CharField(max_length=120, unique=True, verbose_name="Nome")
    description = models.CharField(max_length=500, verbose_name="Descrição")
    
    def __str__(self):
        return self.name
    