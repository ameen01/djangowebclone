from django.shortcuts import render, redirect 
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    print('works ')

    return render(request ,'profile.html')