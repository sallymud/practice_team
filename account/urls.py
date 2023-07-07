from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from account.views import Account, profile, ChangePasswordView

urlpatterns = [
    path('profile', Account, name='profile'),
    path('profile-changed', profile, name='profile-changed'),
    path('password-change', ChangePasswordView.as_view(), name='password_change'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)