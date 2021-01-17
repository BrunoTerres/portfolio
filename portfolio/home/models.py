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
    bio_language = models.ForeignKey("Bio", on_delete=models.SET_NULL, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('language_detail', args=[str(self.id)])

    
    def __str__(self):
        return '{0}'.format(self.name)

class Tool(models.Model):
    name = models.CharField(max_length=100)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    bio_tool = models.ForeignKey("Bio", on_delete=models.SET_NULL, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('tool_detail', args=[str(self.id)])

    def __str__(self):
        return '{0}'.format(self.name)

class Job(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    Tool = models.ManyToManyField('Tool', help_text="Tool used in the Job")
    bio_job = models.ForeignKey("Bio", on_delete=models.SET_NULL, null=True, blank=True)

    def display_tool(self):
        return ', '.join(tool.name for genre in self.tool.all())

    display_tool.short_description = "Tool"

    def get_absolute_url(self):
        return reverse('job_detail', args=[str(self.id)])
    

    def __str__(self):
        return '{0}'.format(self.name)