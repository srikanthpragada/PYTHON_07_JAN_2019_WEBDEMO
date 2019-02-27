from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from demo.models import Title
from demo.serializers import TitleSerializer


def rest_client(request):
    return render(request, 'rest_client.html')


@api_view(['GET', 'POST'])
def title_process(request):
    if request.method == "GET":
        books = Title.objects.all()
        serializer = TitleSerializer(books, many=True)
        # send all titles in the form of json
        return Response(serializer.data)
    else:  # POST, so insert a new row into table
        title_ser = TitleSerializer(data=request.data)
        if title_ser.is_valid():
            title_ser.save()  # insert into table
            return Response(title_ser.data)
        else:
            return Response(title_ser.errors, status=400)  # bad request


@api_view(['GET', 'DELETE'])
def one_title_process(request, id):
    # check whether object is found
    try:
        book = Title.objects.get(id=id)
    except:
        return Response(status=404)  # Send 404 to client

    if request.method == "GET":
        # Convert Python object to Json and send to client
        serializer = TitleSerializer(book)
        return Response(serializer.data)
    else:  # Delete object from Table and send 204 as status code
        book.delete()
        return Response(status=204)  # No data
