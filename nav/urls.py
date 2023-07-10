from django.contrib import admin
from django.urls import path, include
from nav import views


admin.site.site_header = "Portfolio Backend"
admin.site.site_title = "Port Backend"
admin.site.index_title = "Welcome to backdoor of your project :))"


urlpatterns = [
    path('', views.index, name="main"),
    path('aboutme', views.aboutme, name="about"),
    path('projects', views.projects, name="projects"),
    path('contactme', views.contactme, name="contact"),
]
