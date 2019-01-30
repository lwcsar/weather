from django.db import models


class Temperature(models.Model):
    celsius = models.FloatField(default=0.0)
    change = models.FloatField(default=0.0)
    recorded_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.celsius)


class Humidity(models.Model):
    pass


class Pressure(models.Model):
    pressure = models.FloatField(default=0.0)
    change = models.FloatField(default=0.0)
    recorded_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.pressure)
