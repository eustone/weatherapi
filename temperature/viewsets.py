from .models import Temperature
from .serializers import TemperatureSerializer
from rest_framework import viewsets


class TemperatureViewset(viewsets.ModelViewSet):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer
