from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from Simulator.models import Fire
from Simulator.serializers import FireSerializer

# Create your views here.
def say_hello(request):
    return render(request, 'map.html')

class FireViewSet(ModelViewSet):

    serializer_class = FireSerializer
    queryset = Fire.objects.all()
  
    def list(self, request):
        serializer = FireSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = FireSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    http_method_names = ['get', 'post']