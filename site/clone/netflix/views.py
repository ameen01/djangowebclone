from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def gallery(request):
    print('works')

    return render(request, 'galary.html')


def regsitor(request):
    if request.method == 'POST':
        print(request.POST['email'])
        print(request.POST['password'])

    return render(request, 'regsitor.html')


def log_in(request):
    print('user')

    return render(request, 'loogin.html')