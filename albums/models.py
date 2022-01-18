from django.conf import settings
from django.db import models 
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Album(models.Model):
    title_name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    length_in_minutes = models.IntegerField()

    def __str__(self):
        return self.title_name




# Create your models here.
