from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUser(AbstractUser):
    first_name = models.CharField(max_length=255, blank=False)
    email = models.CharField(max_length=255, blank=False)
    address = models.CharField(max_length=255, blank=False)
    postal_code = models.CharField(max_length=12, blank=False)
    telephone = models.CharField(max_length=12)