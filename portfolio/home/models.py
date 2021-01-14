from django.db import models


class DevIntro(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    avatar = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return '{0}'.format(self.name) 


class ProgrammingLanguages(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return '{0}'.format(self.name)

class Technologies(models.Model):
    name = models.CharField(max_length=100)
    language = models.ForeignKey(ProgrammingLanguages, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return '{0}'.format(self.name)

class Projects(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.ManyToManyField(Technologies, help_text="Technologies used in the project")

    def __str__(self):
        return '{0}'.format(self.name)