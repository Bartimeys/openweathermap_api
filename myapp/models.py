from __future__ import unicode_literals

from django.db import models

class City(models.Model):
    name = models.CharField(verbose_name='City', max_length=200)
    latitude = models.FloatField(verbose_name='Latitude')
    longitude = models.FloatField(verbose_name='Longitude')
    # def __str__(self):
    #     return "{0} {1}".format( self.name, self.latitude, self.longitude)

class Weather(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    time = models.IntegerField(verbose_name='Time')
    temperature_max = models.FloatField(verbose_name='Temperature max')
    temperature_min = models.FloatField(verbose_name='Temperature min')
    temperature_day = models.FloatField(verbose_name='Temperature day')
    temperature_night = models.FloatField(verbose_name='Temperature night')
    wind = models.FloatField(verbose_name='Wind')
    cloudiness = models.FloatField(verbose_name='Cloudiness')
    pressure = models.FloatField(verbose_name='Pressure')
    description = models.CharField(verbose_name='Description', max_length=200)
