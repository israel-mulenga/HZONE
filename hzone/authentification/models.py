from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile_photo = models.ImageField()
    phone_number = models.CharField(max_length=10)

