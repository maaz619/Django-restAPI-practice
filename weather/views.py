from rest_framework import generics,views,parsers,status
from rest_framework.response import Response
from weather.models import Weather, WeatherImage
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

class AddWeatherImageView(views.APIView):

    parser_classes=(parsers.MultiPartParser,)

    def post(self,request):
        weather_id=request.data.get('weather_id',None)
        image=request.data.get('image',None)

        try:
            weather=Weather.objects.get(id=weather_id)
            WeatherImage.objects.create(weather=weather,image=image)
            return Response({"success":True},status=status.HTTP_201_CREATED)
        except:
            return Response({"success":False},status=status.HTTP_404_NOT_FOUND)