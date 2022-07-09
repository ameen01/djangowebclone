from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout ,authenticate
from django.contrib.auth.decorators import login_required
from .models import ProfileImg, Post
from django.contrib import messages 
from .forms import UserForm, NewPassword



#test userform model
def regas(request):
    forms = UserForm

    return render(request, 'gelarey.html',)

@login_required(login_url='log_in')
def post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            text = request.POST['text']
            pic = request.FILES.get('file')
            user = request.user
            print(text, f'--------{user}---------',pic)
            # now_post = Post.objects.create()


    return render(request, 'po.html')



# Create your views here.
def home(request):
    posts= Post.objects.all()



    return render(request, 'gelarey.html',{'posts':posts} )

# edit the post
def edid_post(request,pots_uu):
    #find how to get the post id from the user
    # and edite the the post
    #chek if the time its save new time or old 
    if request.user.is_authenticated:
        if request.method == 'POST':
            text = request.POST['text']
            pic = request.FILES.get('file')
            post_id = 'post_uu'
            new_post = Post.objects.get(user=request.user ,id='the post id')
            new_post.image = pic
            new_post.caption = text
            # new_post.save()
    return render(request, 'editpost.html')






#channge the password
#look how to use the models form
def new_pwd(request):
    forms = NewPassword()
    if request.method == 'POST':
        pwdform = NewPassword(request.POST)
        print(pwdform)
        if request.POST['new_password'] == request.POST['comf_password']:
            if pwdform.is_valid():
                user = User.objects.get(pwdform.username.clean)
                user.set_password(pwdform.new_password.clean)
                user.save()
        #     else:
        #         messages.info(request, 'user not exited')
        #         return redirect(new_pwd)
        # else:
        #     messages.info(request , 'password not match')
        #     return redirect(new_pwd)
        # pwdform.username = request.POST['username']
        # pwdform.email = request.POST['email']
        # pwdform.new_password = request.POST['password']
        # pwdform.comf_password = request.POST['password2']


    return render(request ,'newpwd.html',{'forms':forms})


#acatch it to edit user porofile
def upfile(request):
    print('file')
    return render(request , 'upfil.html')





#replace the form the model form filed for more scritey 

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

#replace the form the model form filed for more scritey 
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