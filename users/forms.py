from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import CustomUser


class Registration(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Почта'
    }))

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'surname', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(Registration, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Логин'
        self.fields['username'].help_text = None
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Пароль'
        self.fields['password1'].help_text = None
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Подтвердите пароль'
        self.fields['password2'].help_text = None
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Имя'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Фамилия'
        self.fields['surname'].widget.attrs['class'] = 'form-control'
        self.fields['surname'].widget.attrs['placeholder'] = 'Отчество'


class LoginUserForm(AuthenticationForm):

    username = forms.CharField(widget =
    forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя пользователя'
    }),
    label = ''
    )

    password = forms.CharField(widget = forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль'
    }),
    label = ''
    )