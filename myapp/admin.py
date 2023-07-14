from django.contrib import admin
from .models import CoordinatesDays, CoordinatesHourly, CoordinatesMinutes, Minutes, Hourly, Days

@admin.register(CoordinatesMinutes)
class CoordinatesMinutesAdmin(admin.ModelAdmin):
  list_display = ['latitude', 'longitude', 'time', 'id']

@admin.register(CoordinatesHourly)
class CoordinatesHourlyAdmin(admin.ModelAdmin):
  list_display = ['latitude', 'longitude', 'time', 'id']

@admin.register(CoordinatesDays)
class CoordinatesDaysAdmin(admin.ModelAdmin):
  list_display = ['latitude', 'longitude', 'time', 'id']

@admin.register(Minutes)
class MinutesAdmin(admin.ModelAdmin):
  list_display = ['time', 'precipitate', 'id', 'coordinatesMinutes']

@admin.register(Hourly)
class HourlyAdmin(admin.ModelAdmin):
  list_display = ['time', 'temperature', 'pressure', 'humidity', 'windspeed', 'weather', 'id', 'coordinatesHourly']

@admin.register(Days)
class DaysAdmin(admin.ModelAdmin):
  list_display = ['time', 'maxtemperature', 'mintemperature', 'pressure', 'humidity', 'windspeed', 'weather', 'id', 'coordinatesDays']