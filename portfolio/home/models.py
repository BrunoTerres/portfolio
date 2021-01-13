from django.db import models


class DevIntro(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    avatar = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)