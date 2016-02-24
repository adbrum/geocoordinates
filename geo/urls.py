from django.conf.urls import url
from django.contrib import admin
from geo.core.views import geoCoordenada

urlpatterns = [
    url(r'^$', geoCoordenada, name='home'),
    url(r'^admin/', admin.site.urls),
]
