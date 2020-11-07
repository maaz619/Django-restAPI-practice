from django.conf.urls import url
from weather.views import WeatherRetrieveView,WeatherCreateView, WeathersRetrieveView

urlpatterns=[
    url(r'^weatherapp/all/$',WeatherRetrieveView.as_view()),
    url(r'^weatherapp/create/$',WeatherCreateView.as_view()),
    url(r'^weatherapp/(?P<id>[0-9]+)/$',WeathersRetrieveView.as_view())
]