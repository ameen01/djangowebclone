from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate ,login,logout
from . import models
import requests
from bs4 import BeautifulSoup as bs

# Create your views here.

@login_required(login_url='log_in')
def index(request):
    print('index')
    users = User.objects.all()
    context = {
        'users':users,
        }
    return render(request ,'look.html',context)

@login_required(login_url='log_in')
def gallery(request):
    print('works')
    images = models.Photo.objects.all()
    context =  {
        'images':images,}
    # tex = 'king'
    # r = requests.get(f'https://duckduckgo.com/?q=makeme')
    # soup = bs(r.text,'html.parser')
    # data = soup.prettify()

    return render(request, 'galary.html',{'images':images,})



def regsitor(request):
    if request.method == 'POST':
        a= request.POST['email']
        b= request.POST['username']
        c= request.POST['name']
        d= request.POST['password']
        e= request.POST['repassword']
        if d ==e:
            new_user = User.objects.create_user(username =b, email=a, first_name=c, password=d)
        else:
            print('user not Ex')
        return redirect('gallery')
    return render(request, 'regsitor.html')

def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('gallery')
            print('user done')
        else:
            return redirect('gallery')

    return render(request, 'loogin.html')

@login_required(login_url='log_in')
def logout_user(request):
        logout(request)
        return redirect('index')