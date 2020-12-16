from django.urls import path
from temperature.views import parse_api_data, weather_info

urlpatterns = [

    path('', weather_info, name='weather_info'),
    path('weather/', parse_api_data, name='home'),

]
