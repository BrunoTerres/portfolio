import requests
from django.shortcuts import render
from django.views.generic import TemplateView

from .services import get_github

from home.models import DevIntro, ProgrammingLanguages, Projects, Technologies

def index(request):
    dev = DevIntro.objects.get(id=1)
    projects = Projects.objects.all()
    languages = ProgrammingLanguages.objects.all()
    technologies = Technologies.objects.all()

    context = {
        'dev': dev,
        'projects': projects,
        'languages': languages,
        'technologies': technologies,
    }

    return render(request, 'home/index.html', context)


# class GetGithub(TemplateView):
#     template_name = 'home/github.html'
    
#     def get_context_data(self, *arg, **kwargs):
#         context = {
#             'github': get_github(),
#         }

#         return context


def github_api(request):
   response = requests.get('https://api.github.com/user/1')
   todos = response.json()
   context = {
       'todos': todos,
   }
   return render(request, "home/git_api.html", context)