from django.shortcuts import render

def tests_home(request):
    return render(request, 'tests/tests_home.html')
