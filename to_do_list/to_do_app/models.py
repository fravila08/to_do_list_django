from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

class AppUser(AbstractUser):
    email=models.EmailField( max_length=250, unique=True)  
    # created=models.DateTimeField.
    REQUIRED_FIELDS=[]
    USERNAME_FIELD='email'
    
class To_do(models.Model):
    activity=models.CharField(max_length=100)
    complete=models.BooleanField(default=False)
    created=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.activity}'