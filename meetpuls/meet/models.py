from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import pre_save ,post_save
from django.dispatch import receiver
# Create your models here.


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

# @receiver(pre_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#         instance.ProfileImg.save()