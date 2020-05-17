from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class MenuPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'menu.html')


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        f = UserCreationForm()
        return render(request, 'signup.html', context={'form': f})

    def post(self, request, *args, **kwargs):
        f = UserCreationForm(request.POST)
        if f.is_valid():
            User.objects.create_user(username=f.cleaned_data['username'], password=f.cleaned_data['password1'])
            return redirect('login/')

        return render(request, 'signup.html', {'form': f})


class LoginView(View):
    def get(self, request, *args, **kwargs):
        f = AuthenticationForm()
        return render(request, 'login.html', context={'form': f})

    def post(self, request, *args, **kwargs):
        f = AuthenticationForm(data=request.POST)
        if f.is_valid():
            user = authenticate(username=f.cleaned_data['username'], password=f.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                print("The username and password were incorrect.")
        return render(request, 'login.html', {'form': f})


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')


class ProfilePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')
