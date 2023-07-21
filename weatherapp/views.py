from django.shortcuts import render
from rest_framework import viewsets
from .models import Forecast
from .serializers import ForecastSerializer

class ForecastView(viewsets.ModelViewSet):
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer
    
    