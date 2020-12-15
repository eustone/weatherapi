from typing import Dict, Any

from django.shortcuts import render
from rest_framework.decorators import api_view
import json
import requests
from .serializers import TemperatureSerializer
from .models import Temperature
from .forms import TemperatureForm


# Create your views here.
@api_view(['GET'])
def weather_info(request):
    # get API info from Openweather
    city_name = "Johannesburg"
    api_key = '70a590de7ccaf9c8b489ff228aadba16'
    open_api = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    api_info = requests.get(open_api)
    api = api_info.json()
    max_temp= api['main']['temp_max']
    min_temp= api['main']['temp_min']
    city= api['name']
    print(city)
    temp = Temperature.objects.create(_max_temp=max_temp, _min_temp=min_temp,
                                          _city=city)  # create a Weather object
    temp.save()  # save it

    return render(request, 'index.html', {'api': api})
