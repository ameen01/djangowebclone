import re
from django.shortcuts import render
from django.contrib.auth.models import User 
from django.contrib.auth import login, logout
from . import models


# Create your views here.
def home(request):
    me = User.objects.get(id=2)
    pics = models.ProfileImg.objects.get(user_pic=me)
    print(pics)
    print('home')
    return render(request, 'index.html',{'pics':pics,})

def upfile(request):
    print('file')
    return render(request , 'upfil.html')