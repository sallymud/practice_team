from django.urls import path
from . import views

urlpatterns = [
    path('', views.tests_home, name='tests_home'),
    path('create', views.create, name='create'),
    path('test_list/', views.test_list, name='test_list'),
    path('test_list/<int:test_id>/', views.test_detail, name='test_detail'),
    path('test_list/<int:test_id>/results/', views.test_results, name='test_results'),
]