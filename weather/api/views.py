from rest_framework import generics

from .models import Temperature
from .serializers import TemperatureSerializer

class TemperatureList(generics.ListAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer
    
class TemperatureDetail(generics.RetrieveAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer