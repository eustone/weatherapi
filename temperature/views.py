from typing import Dict, Any
from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
import json
import requests
from .serializers import TemperatureSerializer
from .models import Temperature
from .config import api_key
from .forms import TemperatureForm


# Create your views here.

# Home view
"""#Display normal page and search Results """
def index(request):
    context = {}
    return render(request, 'index.html', context)

# search function
@api_view(['GET'])
def search(request):
    # get API info from Openweather
    global api_key
    try:
        if 'city_name' in request.GET:
            city_name = request.GET.get('city_name')
            api_key = api_key
            open_api = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={api_key}')
            api = open_api.json()
            max_temp = api['main']['temp_max']
            min_temp = api['main']['temp_min']
            city = api['name']
            description = api['weather'][0]['description']
            city_weather = Temperature.objects.create(max_temp=max_temp, min_temp=min_temp,
                                              description=description, city=city)  # create a Weather object
            city_weather.save()  # save it
            city_weather = city_weather
    except Exception as e:
        return HttpResponse('City does not exist')
    return render(request,'index.html',{'city_weather':city_weather})


