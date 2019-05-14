# api/serializers.py
from rest_framework import serializers
from . import models


class TemperatureSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    celsius = serializers.FloatField(default=0.0)
    change = serializers.FloatField(default=0.0)
    recorded_time = serializers.DateTimeField(required=False)

    class Meta:
        fields = ('id', 'celsius', 'change', 'recorded_time')
        model = models.Temperature

    def create(self, validated_data):
        """
        Create and return a new `Temperature` instance, given the validated data.
        """
        return models.Temperature.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Temperature` instance, given the validated data.
        """
        instance.celsius = validated_data.get('celsius', instance.celsius)
        instance.change = validated_data.get('change', instance.change)
        instance.recorded_time = validated_data.get('recorded_time', instance.recorded_time)
        instance.save()
        return instance
        
class HumiditySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'humidity', 'change', 'recorded_time')
        model = models.Humidity

class PressureSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'pressure', 'change', 'recorded_time')
        model = models.Pressure

