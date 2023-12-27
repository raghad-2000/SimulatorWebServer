from rest_framework.serializers import ModelSerializer, IntegerField
 
from Simulator.models import Fire, Sensor, SensorReading

class FireSerializer(ModelSerializer):

    class Meta:
        model = Fire
        fields = ['id', 'lat', 'lon', 'startDate', 'state']
        
class SensorSerializer(ModelSerializer):

    class Meta:
        model = Sensor
        fields = ['id', 'lat', 'lon']

class SensorReadingSerializer(ModelSerializer):
    id = IntegerField(source='sensor.id')

    class Meta:
        model = SensorReading
        fields = ['id', 'data']