from __future__ import unicode_literals

from django.db import models

class Weather(models.Model):
    id = models.IntegerField(primary_key=True)
    city = models.CharField(verbose_name='City', max_length=200)
    latitude = models.CharField(verbose_name='Latitude', max_length=200)
    longitude = models.CharField(verbose_name='Longitude', max_length=200)
    time = models.CharField(verbose_name='Time', max_length=200)
    temperature_max = models.CharField(verbose_name='Temperature', max_length=200)
    temperature_min = models.CharField(verbose_name='Temperature', max_length=200)
    temperature_day = models.CharField(verbose_name='Temperature day', max_length=200)
    temperature_night = models.CharField(verbose_name='Temperature night', max_length=200)
    wind = models.CharField(verbose_name='Wind', max_length=200)
    cloudiness = models.CharField(verbose_name='Cloudiness', max_length=200)
    pressure = models.CharField(verbose_name='Pressure', max_length=200)
    description = models.CharField(verbose_name='Description', max_length=200)

    def __str__(self):
        return "{0}".format(self.city, self.latitude, self.longitude, self.time, self.temperature, self.temperature_day, self.temperature_night, self.wind, self.cloudiness, self.pressure, self.description)