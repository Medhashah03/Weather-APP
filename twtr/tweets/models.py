from django.db import models

class Weather(models.Model):
    place = models.CharField(max_length =70)
    temperature = models.CharField(max_length =70)
    pressure= models.CharField(max_length =70)
    humidity = models.CharField(max_length =70)
# Create your models here.
    def __str__(self):
        return self.place
