from django.shortcuts import render
from .forms import TitleForm


def add_title(request):
    if request.method == "POST":

        # send data from request to form
        f = TitleForm(request.POST)
        if f.is_valid():
            f.save()  # insert row into table
            return render(request, 'add_title.html',
                          {'form' : f,
                           'message' : 'Jobs has been added!'})
    else:  # GET request
        f = TitleForm()

    return render(request, 'add_title.html',{'form' : f})
