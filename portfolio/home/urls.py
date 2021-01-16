from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('jobs/', views.JobListView.as_view(), name='jobs'),
    path('job/<int:pk>', views.JobDetailView.as_view(), name='job_detail'),
    path('tools/', views.ToolListView.as_view(), name='tools'),
    path('tool/<int:pk>', views.ToolDetailView.as_view(), name='tool_detail'),
    path('languages/', views.LanguageListView.as_view(), name='languages'),
    path('language/<int:pk>', views.LanguageDetailView.as_view(), name='language_detail'),
]