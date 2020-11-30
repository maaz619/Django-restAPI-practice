from django.db import models
from account.models import Account
import sys

class Weather(models.Model):
    account=models.ForeignKey(Account,on_delete=models.PROTECT)
    temperature=models.PositiveIntegerField(default=0)
    weather:str=models.CharField(max_length=20,null=True,blank=False)
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now=True)
    
    

class WeatherImage(models.Model):
    weather=models.ForeignKey(Weather,related_name='weather_icon',on_delete=models.PROTECT)
    image=models.FileField(upload_to='image')
