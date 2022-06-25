from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.sing_in, name='sing_in'),
    path('singup/', views.regsitor, name='regsitor'),
    path('updateprofile/', views.updateprofile, name='updateprofile'),
]

