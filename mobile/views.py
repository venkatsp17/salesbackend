from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import data
import json
from main import getallorders, getallcollections, getorder, getpay, getcustomers, createorder, getproducts, createcollection, createcustomer


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


@api_view(['GET'])
def getproduct(request):
    data2 = getproducts()
    return Response(data2)


@api_view(['POST'])
def createord(request):
    data = json.loads(request.body)
    res = createorder(data)
    if (res == "Order Data Created"):
        return Response(res, status=200)
    return Response(res)


@api_view(['POST'])
def createcoll(request):
    data = json.loads(request.body)
    res = createcollection(data)
    if (res == "Collection Data Created"):
        return Response(res, status=200)
    return Response(res)


@api_view(['POST'])
def createcust(request):
    data = json.loads(request.body)
    res = createcustomer(data)
    if (res == "Customer Data Created"):
        return Response(res, status=200)
    return Response(res)
