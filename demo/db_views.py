from django.shortcuts import render
from .forms import TitleForm
from . models import  Title


def add_title(request):
    if request.method == "POST":
        # send data from request to form
        f = TitleForm(request.POST)
        if f.is_valid():
            f.save()  # insert row into table
            return render(request, 'add_title.html',
                          {'form' : f,
                           'message' : 'Title has been added!'})
    else:  # GET request
        f = TitleForm()

    return render(request, 'add_title.html',{'form' : f})


def list_titles(request):
    titles = Title.objects.all()
    print(titles)
    return render(request, 'list_titles.html',{'titles' : titles })