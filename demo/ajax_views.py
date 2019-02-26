from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def ajax_demo(request):
    return render(request, 'ajax_demo.html')


def date_time(request):
    now = datetime.now()
    return HttpResponse(str(now))
