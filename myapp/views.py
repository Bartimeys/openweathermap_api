import json

import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import View

from myapp.models import Weather, City


class SearchCityView(View):
    template_name = 'myapp/search.html'
    success_url = reverse_lazy('search-town')

    def get(self, request):
        return render(request, "myapp/search.html")

    def post(self, request):

        # get data from api
        cityParam = request.POST.get('city', '')

        # http://api.openweathermap.org/data/2.5/forecast/daily?q=London&units=metric&cnt=14&appid=23b63825187c61b018c0b9b735a2d308
        url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q={0}&units=metric&cnt=14&appid={1}'
        appid = '23b63825187c61b018c0b9b735a2d308'
        jsonData = requests.get(url.format(cityParam, appid)).text
        appData = json.loads(jsonData)

        # parse data from api
        cities = City.objects.filter(name=appData['city']['name'])
        if len(cities) == 0:
            city = City()
            city.name = appData['city']['name']
            city.longitude = appData['city']['coord']['lon']
            city.latitude = appData['city']['coord']['lat']
            city.save()
        else:
            city = cities[0]

        weather_info = []
        for item in appData['list']:
            weather = Weather()

            weather.city = city
            weather.temperature_night = item['temp']['night']
            weather.temperature_day = item['temp']['day']
            weather.temperature_min = item['temp']['min']
            weather.temperature_max = item['temp']['max']
            weather.time = item['dt']
            weather.wind = item['speed']
            weather.cloudiness = item['clouds']
            weather.pressure = item['pressure']
            weather.description = item['weather'][0]['description']

            weather.save()
            weather_info.append(weather)

        result = []
        for weather in weather_info:
            item = {}
            item['name'] = city.name
            item['longitude'] = city.longitude
            item['latitude'] = city.latitude
            item['temperature_night'] = weather.temperature_night
            item['temperature_day'] = weather.temperature_day

            item['temperature_min'] = weather.temperature_min
            item['temperature_max'] = weather.temperature_max
            item['time'] = weather.time
            item['wind'] = weather.wind
            item['cloudiness'] = weather.cloudiness
            item['pressure'] = weather.pressure
            item['description'] = weather.description

            result.append(item)

        return JsonResponse(result, safe=False)


# class PressureChart(View):
#     model = Weather
#     template_name = 'myapp/Weather.html'
#
#     def get_data(self, column):
#         query = Weather.objects.all()
#         return getattr(query, column)

class PressureChart(TemplateView):
    template_name = 'myapp/pressure_chart.html'


class GetPressureData(View):
    paginate_by = 10

    def get(self, request):
        weathers = Weather.objects.all()
        result = []
        for weather in weathers:
            item = {}
            item['name'] = weather.city.name
            item['longitude'] = weather.city.longitude
            item['latitude'] = weather.city.latitude
            item['temperature_night'] = weather.temperature_night
            item['temperature_day'] = weather.temperature_day

            item['temperature_min'] = weather.temperature_min
            item['temperature_max'] = weather.temperature_max
            item['time'] = weather.time
            item['wind'] = weather.wind
            item['cloudiness'] = weather.cloudiness
            item['pressure'] = weather.pressure
            item['description'] = weather.description

            result.append(item)

        return JsonResponse(result, safe=False)
