from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile_photo = models.ImageField(blank=True, null=True, upload_to='profile_images/')
    phone_number = models.CharField(max_length=10, blank=True, null=True)

