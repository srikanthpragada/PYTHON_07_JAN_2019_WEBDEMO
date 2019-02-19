from django.http import HttpResponse


# Function view
def hello(request):
    return HttpResponse("<h1 style='color:red'>Hello Django!</h1>")
