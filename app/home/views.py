import requests
import datetime

from django.shortcuts import render, redirect
from django.views import generic
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy

from home.models import Bio, Language, Job, Tool, Contact
from home.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

def index(request):
    return render(request, 'home/index.html')        

def tools(request):

    return render(request, 'home/tools.html')


def languages(request):

    return render(request, 'home/languages.html')



def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message'] 
            full_message = """
                                Name = {}
                                Email = {}
                                Text = {}
            """.format(name, from_email, message)
            
            try:
                send_mail(subject, full_message, from_email, ['brunoeterres@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home:success')
    return render(request, "home/email.html", {'form': form})

def success(request):
    return HttpResponse('Success! Thank you for your message.')

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
    
    
#class ContactCreateView(generic.CreateView):
#    model = Contact
#    form_class = ContactForm
#    success_url = reverse_lazy("thanks")
    
    
def thanks(request):
    return HttpResponse("Thank you! Will get in touch soon.")
    

def image_upload(request):
    
    if request.method == "POST" and request.FILES["image_file"]:
        image_file = request.FILES["image_file"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        print(image_url)
        return render(request, "upload.html", {
            "image_url": image_url
        })
    
    return render(request, "upload.html")