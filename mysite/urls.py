from django.conf.urls import include, url
from django.contrib import admin
#
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'', include('myapp.urls')),
#
# ]
#
# from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^myapp/', include('myapp.urls')),
]
