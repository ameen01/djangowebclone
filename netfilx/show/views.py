from django.shortcuts import render, redirect 
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from requests import request

# Create your views here.

# 1 this page need to display all the images.
# 2 add away to filter the images by catogery
# 2  
def index(request):
    print('works ')

    return render(request ,'profile.html')


# 1 create new user if email and username ont on db
def regsitor(request):
    if request.method == 'POST':
        print('mewuser')
        f_name = request.POST['name']
        l_name = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        pwd = request.POST['password']
        pwd2 = request.POST['rpassword']
        if pwd == pwd2:
            if username not in User.objects.all:
                if email not in User.objects.all:
                    new_user = User.objects.create_user(username=username, email=email, frist_name=f_name ,password=pwd)
                    new_user.save()
                    return redirect('index')


            print('home')
        else:
            print('not')

    return render(request, 'regsitor.html')


# 1 log in the user by email or password.
# 2 look if the user exeitd in the database
# 3 if user not exeit flash masseg to the user
def sing_in(request):
    print('regs')
    return render(request, 'singin.html')



# 1 look how whare the img uplod 
# 2 take img from user and add to db

def updateprofile(request):
    print('pro')
    return render(request, 'profile.html' )

