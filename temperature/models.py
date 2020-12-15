from statistics import mean, median
from django.db.models.signals import pre_save

from django.db import models


# Create your models here.

class Temperature(models.Model):
    _min_temp = models.FloatField(default=0)
    _max_temp = models.FloatField(default=0)
    _average = models.FloatField(default=0, blank=True)
    _median = models.FloatField(default=0, blank=True)
    _city = models.CharField(max_length=255)
    _time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self._city} {self._min_temp} " \
               f"{self._max_temp} {self._average} " \
               f"{self._median} {self._time}"

    class Meta:
        ordering = ['_time']


def max_temperature_receiver_function(sender, instance, *args, **kwargs):
      if instance._max_temp and instance._min_temp:
               instance._average = mean([instance._max_temp, instance._min_temp])


def min_temperature_receiver_function(sender, instance, *args, **kwargs):
    if instance._max_temp and instance._min_temp:
        instance._median = median([instance._max_temp, instance._min_temp])

pre_save.connect(max_temperature_receiver_function, sender=Temperature)

pre_save.connect(min_temperature_receiver_function, sender=Temperature)






