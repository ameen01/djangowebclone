from django.urls import path
from . import views

urlpatterns = [

    path('', views.gallery, name='gallery'),
    path('sinup', views.regsitor, name='regsitor'),
    path('login', views.log_in, name='log_in'),
]