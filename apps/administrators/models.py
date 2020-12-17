from django.db import models
from django.contrib.auth.models import User

import uuid

class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=30, default="administrator")
    token = models.UUIDField(default=uuid.uuid4())
