from django.contrib import admin
from weather.models import Weather,WeatherImage

class WeatherImageInline(admin.TabularInline):
    model=WeatherImage
    fields=("image",)

@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display=('id','weather','temperature')
    inlines=[WeatherImageInline]