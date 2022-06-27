from django.db import models
from django.contrib.auth.models import User

# Create your models here

class ProfileImg(models.Model):
    user_pic = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField( upload_to ='profiles',null=False, blank=True, default= 'avatar.png')
    


