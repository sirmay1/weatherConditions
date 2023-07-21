from rest_framework import serializers
from .models import Forecast

class ForecastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Forecast
        fields = ('id', 'date', 'condition', 'state', 'city')