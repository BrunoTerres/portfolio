from django.urls import path

from . import views

urlpatterns = [
    path('', views.image_upload, name='upload'),
]