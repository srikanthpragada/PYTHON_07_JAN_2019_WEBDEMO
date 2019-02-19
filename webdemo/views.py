from django.http import HttpResponse


# Function view
def hello(request):
    return HttpResponse("<h1 style='color:red'>Hello Django!</h1>")


def wish(request):
    name = request.GET.get("name","Unknown")
    msg = ""
    return HttpResponse(f"<h1>Hello {name}, {msg}</h1>")
