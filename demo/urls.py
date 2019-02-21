
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path("welcome/", views.welcome),
   path("info/", views.course_info),
   path("countries/", views.list_countries),
   path("interest/", views.interest),

]
