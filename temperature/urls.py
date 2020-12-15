from django.urls import path
from temperature.views import parse_api_data

urlpatterns = [
    path('', parse_api_data, name='home')
]
