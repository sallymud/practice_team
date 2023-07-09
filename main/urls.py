from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import LogoutUser

urlpatterns = [
    path('homepage/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('logout/', LogoutUser, name='logout'),
    path('account/', views.account, name='account'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)