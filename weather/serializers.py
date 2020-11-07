from rest_framework.serializers import ModelSerializer
from weather.models import Weather

class WeatherSerializer(ModelSerializer):
    class Meta:
        model=Weather
        read_only_fields=("id","createdAt","updatedAt")
        fields=("id","weather","temperature","createdAt","updatedAt")
