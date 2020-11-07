from rest_framework import generics
from rest_framework.response import Response
from weather.models import Weather
from weather.serializers import WeatherSerializer

class WeatherRetrieveView(generics.ListAPIView):
    serializer_class=WeatherSerializer
    queryset=Weather.objects.all()

class WeatherCreateView(generics.CreateAPIView):
    serializer_class=WeatherSerializer
    queryset=Weather.objects.all()

class WeathersRetrieveView(generics.RetrieveAPIView):
    lookup_field="id"
    queryset=Weather.objects.all()
    serializer_class=WeatherSerializer