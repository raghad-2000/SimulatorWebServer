from rest_framework.serializers import ModelSerializer, SlugRelatedField
 
from Simulator.models import Fire, Sensor

class FireSerializer(ModelSerializer):

    class Meta:
        model = Fire
        fields = ['id', 'x_coord', 'y_coord', 'startDate', 'state']

class SensorDataSerializer(ModelSerializer):

    class Meta:
        model = Sensor
        fields = ['id', 'temperature']

class SensorPositionSerializer(ModelSerializer):

    class Meta:
        model = Sensor
        fields = ['id', 'x_coord', 'y_coord']