from django.db import models

# Create your models here.

# custom user model for future use
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    telephone = models.CharField(max_length=20, blank=True)
    def __str__(self):
        return self.username
    