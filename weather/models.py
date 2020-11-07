from django.db import models

class Weather(models.Model):
    temperature=models.PositiveIntegerField(default=0)
    weather:str=models.CharField(max_length=20,null=True,)
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now=True)