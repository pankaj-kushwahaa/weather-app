from django.db import models

class CoordinatesMinutes(models.Model):
  latitude = models.FloatField(max_length=50)
  longitude = models.FloatField(max_length=50)
  time = models.DateTimeField(auto_now=True)

  def __str__(self) -> str:
    return str(self.id)

class CoordinatesHourly(models.Model):
  latitude = models.FloatField(max_length=50)
  longitude = models.FloatField(max_length=50)
  time = models.DateTimeField(auto_now=True)

  def __str__(self) -> str:
    return str(self.id)

class CoordinatesDays(models.Model):
  latitude = models.FloatField(max_length=50)
  longitude = models.FloatField(max_length=50)
  time = models.DateTimeField(auto_now=True)

  def __str__(self) -> str:
    return str(self.id)

class Minutes(models.Model):
  coordinatesMinutes = models.ForeignKey(CoordinatesMinutes, on_delete=models.CASCADE)
  time = models.DateTimeField()
  precipitate = models.CharField(max_length=20)

class Hourly(models.Model):
  coordinatesHourly = models.ForeignKey(CoordinatesHourly, on_delete=models.CASCADE)
  time = models.DateTimeField()
  temperature = models.IntegerField()
  pressure = models.IntegerField()
  humidity = models.IntegerField()
  windspeed = models.FloatField()
  weather = models.CharField(max_length=30)

class Days(models.Model):
  coordinatesDays = models.ForeignKey(CoordinatesDays, on_delete=models.CASCADE)
  time = models.DateTimeField()
  maxtemperature = models.IntegerField()
  mintemperature = models.IntegerField()
  pressure = models.IntegerField()
  humidity = models.IntegerField()
  windspeed = models.FloatField()
  weather = models.CharField(max_length=30)