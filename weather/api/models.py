from django.db import models


class Temperature(models.Model):
    celsius = models.FloatField(default=0.0)
    change = models.FloatField(default=0.0)
    recorded_time = models.DateTimeField(auto_now=True)


class Humidity(models.Model):
    pass
