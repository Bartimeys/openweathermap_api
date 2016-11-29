import json

import requests
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import FormView
from django.views.generic import UpdateView
from django.views.generic import View
from django.http import JsonResponse

from django.views.generic.edit import CreateView
from myapp.models import Weather


class SearchCityView(View):

    model = Weather
    fields = ['city','latitude','longitude','time','temperature','temperature_day','temperature_night','wind','cloudiness','pressure','description']

    def get(self, request):
        return render(request, "myapp/search.html")

    def post(self, request):
        city = request.POST.get('city', '')
        # http://api.openweathermap.org/data/2.5/forecast/daily?q=London&units=metric&cnt=14&appid=23b63825187c61b018c0b9b735a2d308
        url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q={0}&units=metric&cnt=14&appid={1}'
        appid = '23b63825187c61b018c0b9b735a2d308'
        jsonData = requests.get(url.format(city, appid)).text
        appData = json.loads(jsonData)
        result = {}
        weather = Weather()
        for items in appData['city']:
            if items == 'name':
                result.update({'City': appData['city'][items]})
                weather.city = appData['city'][items]

        for lon in appData['city']['coord']:
            if lon == 'lon':
                result.update({'Longitude': appData['city']['coord'][lon]})
                weather.longitude = appData['city']['coord'][lon]

        for lat in appData['city']['coord']:
            if lat == 'lat':
                result.update({'Latitude': appData['city']['coord'][lat]})
                weather.latitude = appData['city']['coord'][lat]

        for key in appData['list']:
            for t_night in key['temp']:
                if t_night == 'night':
                    result.update({'Temperature night': key['temp']['night']})
                    weather.temperature_night = key['temp']['night']

        for temp in appData['list']:
            for t_max in temp['temp']:
                if t_max == 'max':
                    result.update({'Temperature Max': temp['temp']['max']})
                    weather.temperature_max = temp['temp']['max']

        for temp in appData['list']:
            for t_min in temp['temp']:
                if t_min == 'min':
                    result.update({'Temperature Min': temp['temp']['min']})
                    weather.temperature_min = temp['temp']['min']

        for item in appData['list']:
            for t_day in item['temp']:
                if t_day == 'day':
                    result.update({'Temperature day': item['temp']['day']})
                    weather.temperature_day = item['temp']['day']

        for press in appData['list']:
            for p in press:
                if p == 'pressure':
                    result.update({'Pressure': press['pressure']})
                    weather.pressure = press['pressure']

        for des in appData['list']:
            for el in des['weather']:
                for x in el:
                    if x == 'description':
                        result.update({'Description': el[x]})
                        weather.description = el[x]
        for wind in appData['list']:
            for el in wind:
                if el == 'speed':
                    result.update({'Wind': wind[el]})
                    weather.wind = wind[el]

        for clouds in appData['list']:
            for el in clouds:
                if el == 'clouds':
                    result.update({'Clouds': clouds[el]})
                    weather.cloudiness = clouds[el]

        for time in appData['list']:
            for el in time:
                if el == 'dt':
                    result.update({'Time': time[el]})
                    weather.time = time[el]

        response = {"Name": city, "info": result}
        print(response)
        weather.save()
        return JsonResponse(response)

