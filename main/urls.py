from django.urls import path
from . import views
from .views import LogoutUser

urlpatterns = [
    path('homepage/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('logout/', LogoutUser, name='logout')
]