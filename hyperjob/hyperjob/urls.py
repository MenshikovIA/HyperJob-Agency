"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from hyperjob import views
from resume.views import ResumePageView, CreateResumeView
from vacancy.views import VacancyPageView, CreateVacancyView


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('resume/new', CreateResumeView.as_view()),
    re_path('vacancy/new', CreateVacancyView.as_view()),
    re_path('resumes', ResumePageView.as_view()),
    re_path('vacancies', VacancyPageView.as_view()),
    re_path('signup', views.SignUpView.as_view()),
    re_path('login', views.LoginView.as_view()),
    re_path('logout', views.LogoutView.as_view()),
    re_path('home', views.ProfilePageView.as_view()),
    re_path('', views.MenuPageView.as_view()),
]