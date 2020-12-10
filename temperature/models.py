from django.db import models


# Create your models here.


class Temperature(models.Model):
    min_degrees = models.CharField(default=0)
    max_degrees = models.CharField(default=0)

    def __str__(self):
        return self.max_degrees

    def min(self,degrees):
        return self.min_degrees

    def max(self):
        return self.max_degrees

    def average(self):
        avg = self.max_degrees + self.min_degrees / 2
        return avg

    def median(self):
        pass




