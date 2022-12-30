from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import data
from main import getallorders, getallcollections, getorder, getpay, getcustomers


@api_view(['GET'])
def orders(request):
    data1 = getallorders()
    return Response(data1)


@api_view(['GET'])
def collections(request):
    data2 = getallcollections()
    return Response(data2)


@api_view(['GET'])
def custorder(request, id):
    data2 = getorder(id)
    return Response(data2)


@api_view(['GET'])
def custpay(request, id1):
    data2 = getpay(id1)
    return Response(data2)

@api_view(['GET'])
def getcust(request):
    data2 = getcustomers()
    return Response(data2)
