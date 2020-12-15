from django.urls import path
from .views import weather_info

urlpatterns = [
    path('', weather_info, name='home')
]
