# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=200, verbose_name='City')),
                ('latitude', models.CharField(max_length=200, verbose_name='Latitude')),
                ('longitude', models.CharField(max_length=200, verbose_name='Longitude')),
                ('time', models.CharField(max_length=200, verbose_name='Time')),
                ('temperature_max', models.CharField(max_length=200, verbose_name='Temperature')),
                ('temperature_min', models.CharField(max_length=200, verbose_name='Temperature')),
                ('temperature_day', models.CharField(max_length=200, verbose_name='Temperature day')),
                ('temperature_night', models.CharField(max_length=200, verbose_name='Temperature night')),
                ('wind', models.CharField(max_length=200, verbose_name='Wind')),
                ('cloudiness', models.CharField(max_length=200, verbose_name='Cloudiness')),
                ('pressure', models.CharField(max_length=200, verbose_name='Pressure')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
            ],
        ),
    ]