from doctest import register_optionflag
import email
from tokenize import blank_re
from unicodedata import name
from django.db import models
from flask_sqlalchemy import Model
from sqlalchemy import null

# Create your models here.
    

class Post(models.Model):
    title = models.TextField()
    img_loc = models.ImageField(upload_to='images/')
    date = models.DateTimeField


    def __str__(self):
        return self.title

class User(models,Model):
    name = models.TextField()
    username = models.TextField()
    mail = models.EmailField()
    date = models.DateTimeField

    def __str__(self):
        i ={
             'name': self.name,
             'username': self.username,
             'mail': self.mail,

        }
        return i.values


class Videos(models.Model):
    name = models.TextField
    video_loc = models.FileField
    date = models.DateTimeField


    def __str__(self):
        return self.name