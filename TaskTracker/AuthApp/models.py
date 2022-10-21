from django.contrib.auth.models import User
from django.db import models


class Moderator(models.Model):
    """модель модератора"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
