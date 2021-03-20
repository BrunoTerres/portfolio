from django.urls import path

from . import views

app_name = 'safe'
urlpatterns = [
    path('', views.index, name='home'),
]