from pyexpat.errors import messages
from django.shortcuts import render, redirect 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from requests import request
from . models import ProfileImg

# Create your views here.

def por_text(request):
    if request.method == 'POST':
        pic = request.FILES.get('avatar')
        im =ProfileImg.objects.create(image=pic, user_pic=request.user )
        im.save()
        print('new pic')
    return render(request, 'upfile.html',{})


# 1 this page need to display all the images.
# 2 add away to filter the images by catogery
# 2  
def index(request):
    if request.user.is_authenticated:
        img = ProfileImg.objects.get(user_pic=request.user.id)
        print(img)



    return render(request ,'index.html',{})


# 1 create new user if email and username ont on db
def regsitor(request):
    if request.method == 'POST':
        print('mewuser')
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        email = request.POST['email']
        username = request.POST['username']
        pwd = request.POST['password']
        pwd2 = request.POST['repassword']
        if pwd == pwd2:
            if User.objects.filter(username=username).exists:
                # messages.info(request, 'username in user')
                if User.objects.filter(email=email).exists:
                    print('no email')
                    new_user = User.objects.create_user(username=username,last_name=l_name ,email=email, first_name=f_name ,password=pwd)
                    new_user.save()
                    login(request,new_user)
                    # messages.info(request ,'user created sus')
                    return redirect('index')


            print('home')
        else:
            print('not')

    return render(request, 'regsitor_old.html')


# 1 log in the user by email or password.
# 2 look if the user exeitd in the database
# 3 if user not exeit flash masseg to the user
def sing_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=username, password=pwd)
        if user is not None:
            user = authenticate(username=username, password=pwd)
            login(request,user)
            return redirect('index')
            print('user in')
        else:
            return redirect('sing_in')
    return render(request, 'singin.html')

def sing_out(request):
    logout(request)
    return redirect('index')

# 1 look how whare the img uplod 
# 2 take img from user and add to db

def updateprofile(request):
    if request.method == 'POST':
        print('eeeee') 
    return render(request, 'log.html' ,{})

# change password

def cheange_pwd(request):
    if request.method == 'POST':
        email    = request.POST['email']
        newpwd  = request.POST['new_pwd']
        newpwd2 = request.POST['new_pwd2']
        user = User.objects.get(email=email)
        try:
            if user.email==email:
                if newpwd == newpwd2:
                    user.set_password(newpwd)
                    user.save()
                    login(request, user)
                    return redirect('index')
                    print('new pasowrd')
        except:
            return redirect('cheange_pwd')
            print('new no psss')

    return render(request, 'newpwd.html')

