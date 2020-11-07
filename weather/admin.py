from django.contrib import admin
from weather.models import Weather

@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display=('weather','temperature')