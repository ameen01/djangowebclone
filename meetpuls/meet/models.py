from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import pre_save ,post_save
from django.dispatch import receiver
from datetime import datetime
import uuid
# Create your models here.

# if user careate this filed will be reated
class ProfileImg(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='profiles',null=False, blank=True, default= 'avatar.png')
    age = models.DateTimeField(auto_now_add=True)
    contory = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} ProfileImg'
        
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        ProfileImg.objects.create(user=instance)
        instance.save()


#post that need for posting
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='posts')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    how_many_likes = models.IntegerField(default=0)

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

#  
class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user
# @receiver(pre_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#         instance.ProfileImg.save()