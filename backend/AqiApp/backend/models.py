from django.db import models

# Create your models here.

class BaseModel(models.Model):
    #these two keep track of when a record is created and updated, useful in auditing
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        #this sets the class as an abstract class, making this the template for the classes that follow
        #marking this as abstract also ensures that this doesn't become an actual table in database
        abstract = True

class Location(BaseModel):
    name = models.CharField(max_length=255)
    coordinates = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class AirQuality(models.Model):   
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    aqi = models.IntegerField()
    time = models.DateTimeField()

class Pollutant(models.Model):
    name = models.CharField(max_length = 100)
    max_level = models.FloatField() #max healthy level of pollutant in the air
    
    def __str__(self):
        return self.name

class PM25(models.Model):
    value = models.FloatField()
    air_quality = models.ForeignKey(AirQuality, on_delete = models.CASCADE)

class Ozone(models.Model):
    value = models.FloatField()
    air_quality = models.ForeignKey(AirQuality, on_delete = models.CASCADE)
    
class PollutantMeasurement(models.Model):
    pollutant = models.ForeignKey(Pollutant, on_delete = models.CASCADE)
    value = models.FloatField()
    air_quality = models.ForeignKey(AirQuality, on_delete = models.CASCADE)