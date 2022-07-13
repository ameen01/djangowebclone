from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout ,authenticate
from django.contrib.auth.decorators import login_required
from .models import ProfileImg, Post
from django.contrib import messages 
from .forms import UserForm, NewPassword, UserIN, PostForm



@login_required(login_url='log_in')
def index(request):
   
            # now_post = Post.objects.create()


    return render(request, 'all.html')


# Create your views here.
def home(request):
    posts= Post.objects.all()



    return render(request, 'all.html',{'posts':posts} )



# find  way to not dispaly avatar in the post if the image no fond
def Posting(request):
    image = ProfileImg.objects.reverse
    print(image ,"1111")
    blogs = Post.objects.reverse
    posts= Post.objects.all()
    if request.user.is_authenticated:
        if request.method == 'POST':
            text = request.POST['text']
            post_img = request.FILES.get('post_img')
            user = request.user
            if post_img is not None:
                new_post = Post.objects.create(user=user,caption=text,image=post_img)
                new_post.save()
            else:
                new_post = Post.objects.create(user=user,caption=text)
                new_post.save()
        user =request.user
        blogs= Post.objects.order_by()
        blogs= Post.objects.filter(user=user).reverse()
        image= ProfileImg.objects.get(user=user)
    return render(request, 'home.html',{'image':image, 'blogs':blogs})



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
# lock how to dispaly the erro messg to user
def new_pwd(request):
    forms = NewPassword()
    if request.method == 'POST':
        pwdform  = NewPassword(request.POST)
        username = pwdform.cleaned_data.get('username')
        pwd      = pwdform.cleaned_data.get('password')
        pwd2     = pwdform.cleaned_data.get('password2')
        if pwdform.is_valid():
            if User.objects.filter(username=username).exists():
                if pwd == pwd2:
                    user = User.objects.get(username)
                    user.set_password(pwd)
                    user.save()
                    messages.success(request,'password chande success')
                    return redirect('home')
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





# test the user and make the html file more user frindly
# lock how to dispaly the erro msg to user

def sign_up(request):
    form = UserForm
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username  = form.cleaned_data.get('username')
            email     = form.cleaned_data.get('email')
            f_name    = form.cleaned_data.get('first_name')
            l_name    = form.cleaned_data.get('last_name')
            pwd       = form.cleaned_data.get('password')
            pwd2      = form.cleaned_data.get('password2')

            if User.objects.filter(username=username).exists():
                messages.error(request,'user is in use')
                return redirect('regsitor')
            if User.objects.filter(email=email).exists():
                messages.error(request,'email is in use')
                return redirect('regsitor')
            if pwd == pwd2:
                new_user = User.objects.create_user(email=email, username=username,
                password=pwd, first_name=f_name, last_name=l_name)
                new_user.save()
                messages.success(request,f'welcome {username}')
                login(request ,new_user)
                return redirect('/')
            else:
                messages.error(request,'passowrd not match')
                return redirect('regsitor')    
    return render(request ,'regsitor.html', {'form':form})        


# lock how to dispaly the erro msg to user
def  log_in(request):
    form = UserIN()
    if request.method == 'POST':
        form = UserIN(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')
            if User.objects.filter(username=username).exists():
                user= authenticate(request, username=username ,password=pwd)
                if user is not None:
                    login(request, user)
                    messages.success(request,' welacome back')
                    return redirect('home')
            else:
                messages.error(request, 'username or password are wrong')
                return redirect('singin')

    return render(request, 'singin.html',{'form':form})


@login_required(login_url='sign_in')
def log_out(request):
    logout(request)
    return redirect('home')



@login_required(login_url='sign_in')
def load_profile(request):
    pro= ProfileImg.objects.get(user=request.user)
    print('por')
    return render(request, 'profile.html',{'pro':pro})