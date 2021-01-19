from django.db import models
from django.urls import reverse


class Bio(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    avatar = models.ImageField()

    def __str__(self):
        return '{0}'.format(self.name) 


class Language(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    img =  models.ImageField()

    def get_absolute_url(self):
        return reverse('language_detail', args=[str(self.id)])

    
    def __str__(self):
        return '{0}'.format(self.name)

class Tool(models.Model):
    name = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('tool_detail', args=[str(self.id)])

    def __str__(self):
        return '{0}'.format(self.name)

class Job(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    Tool = models.ManyToManyField(Tool, help_text="Tool used in the Job")


    def display_tool(self):
        return ', '.join(tool.name for genre in self.tool.all())

    display_tool.short_description = "Tool"

    def get_absolute_url(self):
        return reverse('job_detail', args=[str(self.id)])
    

    def __str__(self):
        return '{0}'.format(self.name)
    
    
    
class Contact(models.Model):
    first_name =  models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    
    class Meta:
        ordering = ["last_name"]
        
    def __str__(self):
        return '{0}, {1}'.format(self.first_name, self.last_name)
        