from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout ,authenticate
from django.contrib.auth.decorators import login_required
from .models import ProfileImg
from django.contrib import messages 
from .forms import UserForm



#test userform model
def regas(request):
    forms = UserForm()

    return render(request, 'all.html',)



# Create your views here.
def home(request):
    s= ProfileImg.objects.get(user=request.user)
    print(s.image)



    return render(request, 'index.html',{'s':s} )




def upfile(request):
    print('file')
    return render(request , 'upfil.html')






def sign_up(request):
    if request.method == 'POST':
        username  = request.POST['username']
        email     = request.POST['email']
        f_name    = request.POST['f_name']
        l_name    = request.POST['l_name']
        pwd       = request.POST['password']
        pwd2      = request.POST['repassword']
        "fix the location of the passowrd"
        
        if User.objects.filter(username=username).exists():
            messages.info(request,'usernmae is in use')
            return redirect('regsitor')
        if User.objects.filter(email=email).exists():
            messages.info(request,'email in use')
            return redirect('regsitor')
        if pwd ==pwd2:
            new_user = User.objects.create_user(username=username,email=email, password=pwd, first_name=f_name,last_name=l_name)
            new_user.save()
            user_model = User.objects.get(username=username)
            # default_pro = ProfileImg.objects.create(user_pic=user_model)
            # default_pro.save()
            login(request, new_user)
            messages.info(request,'user creatred')
            return redirect('home')
        else:
            messages.info(request,'password not match')
        return redirect('regsitor')
    return render(request ,'regsitor_old.html')        


def  log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        pwd = request.POST['password']
        me   = User.objects.get(username=username)
        user= authenticate(request, username=username ,password=pwd)
        if user is not None:
            login(request, user)
            messages.info(request,' welacome back')
            return redirect('home')
        else:
            messages.info(request, 'username or password are wrong')
            return redirect('singin')

    return render(request, 'singin.html')



@login_required(login_url='sign_in')
def log_out(request):
    logout(request)
    return redirect('home')



@login_required(login_url='sign_in')
def load_profile(request):
    pro= ProfileImg.objects.get(user=request.user)
    print('por')
    return render(request, 'profile.html',{'pro':pro})