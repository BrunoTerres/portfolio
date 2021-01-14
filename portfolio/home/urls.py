from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('github/', views.github_api, name='git-hub')
]
