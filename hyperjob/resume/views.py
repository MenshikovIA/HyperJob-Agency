from django.shortcuts import render, redirect
from django.views import View
from resume.models import Resume
from django.http import HttpResponseForbidden


class ResumePageView(View):
    def get(self, request, *args, **kwargs):
            return render(request, 'resumes.html',
                          context={'resumes': Resume.objects.all()})


class CreateResumeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'resume/new.html')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and not request.user.is_staff:
            Resume.objects.create(author=request.user, description=request.POST["description"])
            return redirect('home/')
        return HttpResponseForbidden()
