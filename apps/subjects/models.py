from django.db import models

from apps.teachers.models import Teacher

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100)
    schedule = models.TimeField(auto_now=False, auto_now_add=False)
    capacity = models.IntegerField()
    description = models.CharField(max_length=2000)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name