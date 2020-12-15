from django.forms import ModelForm, TextInput
from .models import Temperature

class TemperatureForm(ModelForm):
    class Meta:
        model = Temperature
        fields = ['city']
        widgets = {'name':TextInput(attrs={'class':'input','placeholder':'City Name'})}

