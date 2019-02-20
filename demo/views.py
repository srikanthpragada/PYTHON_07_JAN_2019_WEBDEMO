from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
import requests

# Create your views here.

def welcome(request):
    return HttpResponse("<h1>Welcome!</h1>")


def course_info(request):
    c = Course("Python",4000,40)
    return render(request, 'course_info.html', {'course' : c})


def list_countries(request):
    resp = requests.get("https://restcountries.eu/rest/v2/all")
    countries = resp.json()
    #asian = list(filter(countries, lambda c : c['region'] == 'Asia'))
    #countries, lambda c : c['region'] == 'Asia'))
    return render(request, 'countries.html',
                  {'countries' : countries})