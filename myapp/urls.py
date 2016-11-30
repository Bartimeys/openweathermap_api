from django.conf.urls import url

from myapp.views import SearchCityView, PressureChart, GetPressureData

urlpatterns = [
    url(r'^myapp/$', SearchCityView.as_view(), name='search-town'),
    url(r'^pressure-chart/$', PressureChart.as_view(), name='pressure-chart'),
    url(r'^pressure-data/$', GetPressureData.as_view(), name='pressure-data'),
]