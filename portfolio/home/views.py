import requests
from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse

from home.models import Bio, Language, Job, Tool


def index(request):
    dev = Bio.objects.get(id=1)
    jobs = Job.objects.all()
    languages = Language.objects.all()
    tools = Tool.objects.all()

    context = {
        'dev': dev,
        'jobs': jobs,
        'languages': languages,
        'tools': tools,
    }

    return render(request, 'home/index.html', context)

class JobListView(generic.ListView):
    model = Job
    context_object_name = 'job_list'
    queryset = Job.objects.all()
    templalte_name = "home/job_list.html"


class JobDetailView(generic.DetailView):
    model = Job
    template_name = "home/job_detail.html"
    

class ToolListView(generic.ListView):
    model = Tool
    context_object_name = 'tool_list'
    queryset = Tool.objects.all()
    templalte_name = "home/tool_list.html"


class ToolDetailView(generic.DetailView):
    model = Tool
    template_name = "home/tool_detail.html"
    
    

class LanguageListView(generic.ListView):
    model = Language
    context_object_name = 'language_list'
    queryset = Language.objects.all()
    templalte_name = "home/anguage_list.html"


class LanguageDetailView(generic.DetailView):
    model = Language
    template_name = "home/language_detail.html"