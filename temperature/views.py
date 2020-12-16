from typing import Dict, Any

from django.shortcuts import render, HttpResponse
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
    city_name = "London"
    api_key = '70a590de7ccaf9c8b489ff228aadba16'
    open_api = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    api_info = requests.get(open_api)
    api = api_info.json()
    print(api)
    max_temp= api['main']['temp_max']
    min_temp= api['main']['temp_min']
    city= api['name']
    temp = Temperature.objects.create(max_temp=max_temp, min_temp=min_temp,
                                          city=city)  # create a Weather object
    temp.save()  # save it
    return HttpResponse("Weather API data saved.")


def parse_api_data(request):
    api_data = Temperature.objects.last()
    print(api_data)
    return render(request, 'index.html', {'api': api_data})
