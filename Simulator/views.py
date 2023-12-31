from django.shortcuts import render

from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import action

from Simulator.models import Fire, Sensor, SensorReading
from Simulator.serializers import FireSerializer, SensorSerializer, SensorReadingSerializer

# Create your views here.
def map(request):
    list_sensors = Sensor.objects.all()
    serializer = SensorSerializer(list_sensors, many=True)

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

    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()

    def create(self, request):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)

    @action(methods=['delete'], detail=False)
    def delete(self, request):
        count = Sensor.objects.all().delete()
        return Response({'message': '{} sensors were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

    http_method_names = ['get', 'post', 'delete']
    
class SensorReadingViewSet(ModelViewSet):

    serializer_class = SensorReadingSerializer
    queryset = SensorReading.objects.all()

    def create(self, request):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)

    http_method_names = ['get', 'post']