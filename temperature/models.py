from statistics import mean, median
from django.db.models.signals import pre_save

from django.db import models


# Create your models here.

class Temperature(models.Model):
    max_temp = models.FloatField(default=0)
    min_temp = models.FloatField(default=0)
    average = models.FloatField(default=0, blank=True)
    median = models.FloatField(default=0, blank=True)
    city = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} {self.min_temp} " \
               f"{self.max_temp} {self.average} " \
               f"{self.median} {self.time}"

    class Meta:
        ordering = ['time']


def max_temperature_receiver_function(sender, instance, *args, **kwargs):
      if instance.max_temp and instance.min_temp:
               instance._average = mean([instance.max_temp, instance.min_temp])


def min_temperature_receiver_function(sender, instance, *args, **kwargs):
    if instance.max_temp and instance.min_temp:
        instance._median = median([instance.max_temp, instance.min_temp])

pre_save.connect(max_temperature_receiver_function, sender=Temperature)

pre_save.connect(min_temperature_receiver_function, sender=Temperature)






