from django.conf.urls import url
from myapp.views import SearchCityView

from . import views

urlpatterns = [
    url(r'^$', SearchCityView.as_view(), name='search-town'),
]