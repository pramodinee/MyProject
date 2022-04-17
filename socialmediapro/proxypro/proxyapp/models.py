from django.db import models
from django.db.models.fields import proxy

class Student (models.Model):
    name = models.CharField(max_length=30)
    mark = models.IntegerField()
    location = models.CharField(max_length=30)

class StudentProxy(Student):
    class Meta:
        proxy = True
