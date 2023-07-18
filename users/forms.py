from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import CustomUser


class Registration(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Почта'
    }))
    creator = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'custom-checkbox'}))
    teacher = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'custom-checkbox'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'surname', 'email', 'password1', 'password2', 'creator', 'teacher')

    def __init__(self, *args, **kwargs):
        super(Registration, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Логин'
        self.fields['username'].label = ''
        self.fields['username'].help_text = None
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Пароль'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = None
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Подтвердите пароль'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = None
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Имя'
        self.fields['first_name'].label = ''
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Фамилия'
        self.fields['last_name'].label = ''
        self.fields['surname'].widget.attrs['class'] = 'form-control'
        self.fields['surname'].widget.attrs['placeholder'] = 'Отчество'
        self.fields['surname'].label = ''
        self.fields['email'].label = ''
        self.fields['creator'].label = 'Составитель тестов'
        self.fields['teacher'].label = 'Преподаватель'


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