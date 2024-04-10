from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import StaticHTMLRenderer



@api_view(['GET'])
@renderer_classes([StaticHTMLRenderer])
def start(request):
    return Response("<h1>SALES APP</h1>")