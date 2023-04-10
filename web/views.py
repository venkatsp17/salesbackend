from rest_framework.decorators import api_view
from rest_framework.response import Response
from main import agetallorders, agetallcollections
# Create your views here.


@api_view(['GET'])
def orders1(request):
    data1 = agetallorders()
    return Response(data1)


@api_view(['GET'])
def collections1(request):
    data1 = agetallcollections()
    return Response(data1)
