from re import L
from turtle import clear
from django.shortcuts import render, redirect
import os

l  =  '/static/base/assets/images/'

# def imge_file(location):
#     loca = os.listdir(f'{location}')
#     all_img = []
#     for file in loca:
#         file = str(file).lower()
#         if '.png' in file:
#             all_img.append(file)
#         elif 'jpg' in file:
#             all_img.append(file)
#     return all_img



def home(request):
    images = {'anem':'home',
               'sol': 'hal9', 
                }
    return render(request,'galary.html',{'images':images})



def index(request):
    return redirect(request, 'index.html' )