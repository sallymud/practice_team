from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from users.models import CustomUser


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('surname', 'creator', 'teacher')}),
    )

    list_display = ("username", "email", "first_name", "last_name", "creator", "teacher", "is_staff")


admin.site.register(CustomUser, CustomUserAdmin)