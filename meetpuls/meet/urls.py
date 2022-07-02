from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('propic/', views.upfile, name='pro'),
    # path('login/', views.sing_in, name='sing_in'),
    # path('singup/', views.regsitor, name='regsitor'),
    # path('logout/', views.sing_out, name='sing_out'),
    # path('reaset/', views.cheange_pwd, name='new_pwd'),
    # path('profile/', views.updateprofile, name='updateprofile'),
]
