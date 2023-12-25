from django.shortcuts import render
from django.core import serializers

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

from Simulator.models import Fire, Sensor
from Simulator.serializers import FireSerializer, SensorSerializer, SensorDataSerializer, SensorPositionSerializer

# Create your views here.
def say_hello(request):
    list_sensors = Sensor.objects.all()
    serializer = SensorPositionSerializer(list_sensors, many=True)

    context = {'list_sensors': JSONRenderer().render(serializer.data).decode("utf-8")}
    return render(request, 'map.html', context)

class FireViewSet(ModelViewSet):

    serializer_class = FireSerializer
    queryset = Fire.objects.all()

    def create(self, request):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)

    http_method_names = ['get', 'post']

class SensorViewSet(ModelViewSet):

    queryset = Sensor.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            if  'data' in self.request.query_params:
                return SensorDataSerializer
            elif 'position' in self.request.query_params:
                return SensorPositionSerializer

        return SensorSerializer

    def create(self, request):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)

    http_method_names = ['get', 'post']