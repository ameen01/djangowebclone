from re import T
from tkinter import N
from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Photos(models.Model):
    category = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()

class ProfileImg(models.Model):
    user_img = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)