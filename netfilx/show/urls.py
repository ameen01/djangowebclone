from django.urls import path
from . import views



urlpatterns = [
    path('', views.por_text, name='pro'),
    path('index/', views.index, name='index'),
    path('login/', views.sing_in, name='sing_in'),
    path('singup/', views.regsitor, name='regsitor'),
    path('logout/', views.sing_out, name='sing_out'),
    path('reaset/', views.cheange_pwd, name='new_pwd'),
    path('profile/', views.updateprofile, name='updateprofile'),
]

