from django.urls import path
from . import views
from users.views import test_creator, test_taker, test_grader

urlpatterns = [
    path('', views.tests_home, name='tests_home'),
    path('create', views.create, name='create'),
    path('test_list/', views.test_list, name='test_list'),
    path('test_list/<int:test_id>/', views.test_detail, name='test_detail'),
    path('test_list/<int:test_id>/results/', views.test_results, name='test_results'),
    path('test_creator/', test_creator, name='test_creator'),
    path('test_taker/', test_taker, name='test_taker'),
    path('test_grader/', test_grader, name='test_grader'),
]