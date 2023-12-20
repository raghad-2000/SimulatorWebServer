from rest_framework.serializers import ModelSerializer, SlugRelatedField
 
from Simulator.models import Fire

class FireSerializer(ModelSerializer):

    class Meta:
        model = Fire
        fields = ['id', 'x_coord', 'y_coord', 'startDate', 'state']