from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import Registration, LoginUserForm


class SignUpView(CreateView):
    form_class = Registration
    success_url = reverse_lazy('Sign_In')
    template_name = 'users/sign_up.html'

    def registration(request):
        form = None
        if request.method == 'POST':
            form = Registration(request.POST)
            email = request.POST.get('email')
            if Registration.objects.filter(email=email).exists():
                messages.error(request, 'Данная почта уже используется!')
            else:
                if form.is_valid():
                    ins = form.save()
                    username = form.cleaned_data['username']
                    password = form.cleaned_data['password1']

                    user = authenticate(username=username, password=password, email=email)
                    ins.email = email
                    ins.save()
                    form.save_m2m()
                    messages.success(request, 'Регистрация прошла успешно')
                    return redirect('Sign_In')

        else:
            form = Registration()

        context = {'form': form}
        return render(request, 'users/sign_up.html', context)


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/sign_in.html'


def Homepage(request):
    return render(request, 'main/homepage.html')