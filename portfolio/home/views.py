from django.shortcuts import render
#from django.views import generic

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


# class IndexView(generic.TemplateView):
#     dev = DevIntro.objects.all()

#     context = {
#         'dev': dev,
#     }
    
#     template_name = "home/index.html"