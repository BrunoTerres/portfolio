import requests
import datetime
from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy

from home.models import Bio, Language, Job, Tool, Contact


def index(request):
    
    try:  
        dev = Bio.objects.get(id=1)
        jobs = Job.objects.all()
        languages = Language.objects.all()
        tools = Tool.objects.all()
        time = datetime.datetime.now()
    except:
        return render(request, 'info_missing.html')
    else:
        context = {
            'dev': dev,
            'jobs': jobs,
            'languages': languages,
            'tools': tools,
            'time': time,
        }

        return render(request, 'home/index.html', context)        

class BioView(generic.TemplateView):
    template_name = "home/bio.html"

class SafeView(generic.TemplateView):
    template_name = "home/safe.html"

class FastView(generic.TemplateView):
    template_name = "home/fast.html"
    
class ResponsiveView(generic.TemplateView):
    template_name = "home/responsive.html"


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
    
    
class ContactCreateView(generic.CreateView):
    model = Contact
    fields = ["first_name", "last_name", "email", "message"]
    success_url = reverse_lazy("thanks")
    
    
def thanks(request):
    return HttpResponse("Thank you! Will get in touch soon.")
    