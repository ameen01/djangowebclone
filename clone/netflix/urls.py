from django.urls import path
from . import views

urlpatterns = [

    path('', views.gallery, name='gallery'),
    path('index/', views.index, name='index'),

    path('sinup/', views.regsitor, name='regsitor'),
    path('logout/', views.logout_user, name='logout_user'),
    path('login/', views.log_in, name='log_in'),
    
]