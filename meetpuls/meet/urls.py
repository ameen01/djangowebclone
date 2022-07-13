from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('posting/', views.Posting, name='postsing'),
    path('propic/', views.upfile, name='pro'),
    path('login/', views.log_in, name='singin'),
    path('signup/', views.sign_up, name='regsitor'),
    path('logout/', views.log_out, name='sing_out'),
    path('reaset/', views.new_pwd, name='newpwd'),
    path('profile/', views.load_profile, name='user_profile'),
]
