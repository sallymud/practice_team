from django.urls import path

from users.views import SignUpView, LoginUser, Homepage

urlpatterns = [
    path('registration', SignUpView.as_view(), name='Sign_Up'),
    path('', LoginUser.as_view(), name='Sign_In'),
    path('homepage', Homepage, name='homepage'),
    ]