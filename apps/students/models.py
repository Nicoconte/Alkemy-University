from django.db import models
from django.contrib.auth.models import User
from apps.subjects.models import Subject

import uuid

# Create your models here.
class Student(models.Model):
    student_account = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dni = models.CharField(max_length=100, null=True, unique=True)
    role = models.CharField(max_length=20, default="student")
    token = models.UUIDField(default=uuid.uuid4(), unique=True)
    
    def __str__(self):
        return self.name

#Connect subjects with the student in a relation one to many
class StudentSubject(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.name} | {self.subject.name}"