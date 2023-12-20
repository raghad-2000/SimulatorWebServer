from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from Simulator.models import Fire
from Simulator.serializers import FireSerializer

# Create your views here.
def say_hello(request):
    return render(request, 'map.html')

class FireViewSet(ModelViewSet):

    serializer_class = FireSerializer

    def get_queryset(self, read_only='True'):
        return Fire.objects.all()

    http_method_names = ['get', 'post']