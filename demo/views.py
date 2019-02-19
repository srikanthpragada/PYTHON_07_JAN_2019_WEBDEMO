from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def welcome(request):
    return HttpResponse("<h1>Welcome!</h1>")


def course_info(request):
    return render(request, 'course_info.html')
