from rest_framework import serializers
from .models import Temperature


class TemperatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Temperature
        fields = '__all__' 


