
from django.contrib import admin
from django.urls import path
from . import views, hr_views,db_views, ajax_views, rest_views

urlpatterns = [
   path("welcome/", views.welcome),
   path("info/", views.course_info),
   path("countries/", views.list_countries),
   path("interest/", views.interest),
   path("interest2/", views.interest2),
   path("listjobs/", hr_views.list_jobs),
   path("addtitle/", db_views.add_title),
   path("list_titles/", db_views.list_titles),
   path("ajaxdemo/", ajax_views.ajax_demo),
   path("datetime/", ajax_views.date_time),

   # REST urls
   path("titles/", rest_views.title_process),
   path("titles/<int:id>/", rest_views.one_title_process),
   path("restclient/", rest_views.rest_client),

]
