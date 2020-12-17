from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    is_active = models.BooleanField()
    
    def __str__(self):
        return self.name