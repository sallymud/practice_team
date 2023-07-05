from django.contrib.auth import logout
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'main/homepage.html')

def about(request):
    return render(request, 'main/about.html')

def account(request):
    return render(request, 'main/account.html')

def LogoutUser(request):
    logout(request)
    return redirect('/')