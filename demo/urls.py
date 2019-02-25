
from django.contrib import admin
from django.urls import path
from . import views, hr_views,db_views

urlpatterns = [
   path("welcome/", views.welcome),
   path("info/", views.course_info),
   path("countries/", views.list_countries),
   path("interest/", views.interest),
   path("interest2/", views.interest2),
   path("listjobs/", hr_views.list_jobs),
   path("addtitle/", db_views.add_title),
   path("titles/", db_views.list_titles),

]
