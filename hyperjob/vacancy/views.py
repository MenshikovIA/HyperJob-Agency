from django.shortcuts import render, redirect
from django.views import View
from vacancy.models import Vacancy
from django.http import HttpResponseForbidden

class VacancyPageView(View):
    def get(self, request, *args, **kwargs):
            return render(request, 'vacancies.html',
                          context={'vacancies': Vacancy.objects.all()})


class CreateVacancyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancy/new.html')
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            Vacancy.objects.create(author=request.user, description=request.POST["description"])
            return redirect('home/')
        return HttpResponseForbidden()
