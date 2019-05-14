from rest_framework import generics

from . import models, serializers
# from .serializers import TemperatureSerializer

class TemperatureList(generics.ListCreateAPIView):
    queryset = models.Temperature.objects.all()
    serializer_class = serializers.TemperatureSerializer
    
class TemperatureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Temperature.objects.all()
    serializer_class = serializers.TemperatureSerializer

class HumidityList(generics.ListCreateAPIView):
    queryset = models.Humidity.objects.all()
    serializer_class = serializers.HumiditySerializer

class HumidityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Humidity.objects.all()
    serializer_class = serializers.HumiditySerializer

class PressureList(generics.ListCreateAPIView):
    queryset = models.Pressure.objects.all()
    serializer_class = serializers.PressureSerializer

class PressureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Pressure.objects.all()
    serializer_class = serializers.PressureSerializer

