from django.db import models
from django.db.models import fields
from rest_framework.fields import ReadOnlyField, SerializerMethodField
from rest_framework.serializers import ModelSerializer ,SerializerMethodField
from weather.models import Weather,WeatherImage



class WeatherImageSerializer(ModelSerializer):

    image_url= SerializerMethodField(method_name='get_image_url')

    def get_image_url(self,weatherImage):
        if weatherImage.image:
            return weatherImage.image.url
        else:
            return None
        
    class Meta:
        model=WeatherImage
        fields=('id','image_url')

class WeatherSerializer(ModelSerializer):
    weather_images=WeatherImageSerializer(source='weather_icon',many=True ,read_only=True)

    class Meta:
        model=Weather
        read_only_fields=("id","createdAt","updatedAt")
        fields=("id","weather","temperature","createdAt","updatedAt","weather_images")