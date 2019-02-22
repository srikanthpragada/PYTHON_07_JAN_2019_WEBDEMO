
from django.contrib import admin
from django.urls import path
from . import views, hr_views

urlpatterns = [
   path("welcome/", views.welcome),
   path("info/", views.course_info),
   path("countries/", views.list_countries),
   path("interest/", views.interest),
   path("interest2/", views.interest2),
   path("listjobs/", hr_views.list_jobs),

]
