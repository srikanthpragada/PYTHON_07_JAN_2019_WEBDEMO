from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
import requests
from .forms import InterestForm


# Create your views here.

def welcome(request):
    return HttpResponse("<h1>Welcome!</h1>")


def course_info(request):
    c = Course("Python", 4000, 40)
    return render(request, 'course_info.html', {'course': c})


def list_countries(request):
    resp = requests.get("https://restcountries.eu/rest/v2/all")
    countries = resp.json()
    asian = filter(lambda c: c['region'] == 'Asia', countries)
    return render(request, 'countries.html',
                  {'countries': asian})


def interest(request):
    # if input is present then process
    if request.method == "POST":
        amount = int(request.POST['amount'])
        period = int(request.POST['period'])
        interest = amount * (period / 12) * 10 / 100
        return render(request, 'interest.html',
                      {"interest": interest,
                       "amount": amount,
                       "period": period})
    else:  # GET request
        return render(request, 'interest.html')


def interest2(request):
    print(request.method)
    if request.method == "POST":
        print("handling post")
        # send data from request to form
        f = InterestForm(request.POST)
        if f.is_valid():
            # take data from form
            amount = f.cleaned_data["amount"]
            period = f.cleaned_data["period"]
            interest = amount * (period/12) * 10 / 100
            print("interest", interest)
            return render(request, 'interest2.html',
                          {'form' : f, 'interest' : interest})
    else:  # GET request
        f = InterestForm()

    return render(request, 'interest2.html',{'form' : f})
