from django.shortcuts import render

def home(request):
    return render(request, 'main/homepage.html')

def about(request):
    return render(request, 'main/about.html')