from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=True,null=True, auto_now=False, auto_now_add=False)
    phone_number = models.CharField(blank=True,null=True,max_length=10)
