from .models import (CoordinatesDays, CoordinatesHourly, CoordinatesMinutes, Minutes, Hourly, Days )
from .helper import getMinutes, getDays, getHours
from datetime import datetime, timedelta

number_of_minutes = 20

def checkMinutesAndSave(lat, lon):
  current_time  = datetime.today()
  new_time = (current_time - timedelta(minutes=number_of_minutes))
  coordinates = CoordinatesMinutes.objects.filter(latitude=lat, longitude=lon)
  if coordinates.exists():
    coordinate = CoordinatesMinutes.objects.filter(latitude=lat, longitude=lon, time__gt=new_time)
    if coordinate.exists():
      print("Data is Relevant")
      queryset = Minutes.objects.filter(coordinatesMinutes=coordinate.first())
    else:
      data = getMinutes(lat, lon)
      print(coordinates)
      print("Data is not Relevant, Data is Updating")
      coordinates.update(latitude=lat, longitude=lon, time=datetime.now())
      minutely = data.get('minutely')
      for minute in minutely:
        dt = datetime.fromtimestamp(int(minute.get('dt')))
        precipi = int(minute.get('precipitation'))
        Minutes.objects.filter(coordinatesMinutes=coordinates.first()).update(time=dt, precipitate=precipi)
      queryset = Minutes.objects.filter(coordinatesMinutes=coordinates.first())
  else:
    print("New Data Creating")
    data = getMinutes(lat, lon)
    coordinates = CoordinatesMinutes.objects.create(latitude=lat, longitude=lon, time=datetime.now())
    print(coordinates)
    minutely = data.get('minutely')
    for minute in minutely:
      dt = datetime.fromtimestamp(int(minute.get('dt')))
      precipi = int(minute.get('precipitation'))
      Minutes.objects.create(coordinatesMinutes=coordinates, time=dt, precipitate=precipi)
    queryset = Minutes.objects.filter(coordinatesMinutes=coordinates.id)
  return queryset

def checkHourAndSave(lat, lon):
  current_time  = datetime.today()
  new_time = (current_time - timedelta(minutes=number_of_minutes))
  coordinates = CoordinatesHourly.objects.filter(latitude=lat, longitude=lon)
  if coordinates.exists():
    print("Coordinates Exists")
    coordinate = CoordinatesHourly.objects.filter(latitude=lat, longitude=lon, time__gt=new_time)
    if coordinate.exists():
      print("Data is Relevant")
      queryset = Hourly.objects.filter(coordinatesHourly=coordinate.first())
    else:
      data = getHours(lat, lon)
      print(coordinates)
      print("Data is not Relevant, Data is Updating")
      coordinates.update(latitude=lat, longitude=lon, time=datetime.now())
      hours = data.get('hourly')
      for hour in hours:
        dt = datetime.fromtimestamp(int(hour.get('dt')))
        temperature = hour.get('temp')
        pressure = int(hour.get('pressure'))
        humidity = int(hour.get('humidity'))
        windspeed = int(hour.get('wind_speed'))
        weather = hour.get('weather')[0].get('main')
        Hourly.objects.filter(coordinatesHourly=coordinates.first()).update(time=dt, temperature=temperature, pressure=pressure, humidity=humidity, windspeed=windspeed, weather=weather)
      queryset = Hourly.objects.filter(coordinatesHourly=coordinates.first())
  else:
    print("New Data Creating")
    data = getHours(lat, lon)
    coordinates = CoordinatesHourly.objects.create(latitude=lat, longitude=lon, time=datetime.now())
    print(coordinates)
    hours = data.get('hourly')
    for hour in hours:
      dt = datetime.fromtimestamp(int(hour.get('dt')))
      temperature = hour.get('temp')
      pressure = int(hour.get('pressure'))
      humidity = int(hour.get('humidity'))
      windspeed = int(hour.get('wind_speed'))
      weather = hour.get('weather')[0].get('main')
      Hourly.objects.create(coordinatesHourly=coordinates, time=dt, temperature=temperature, pressure=pressure, humidity=humidity, windspeed=windspeed, weather=weather)
    queryset = Hourly.objects.filter(coordinatesHourly=coordinates)
  return queryset

def checkDaysAndSave(lat, lon):
  current_time  = datetime.today()
  new_time = (current_time - timedelta(minutes=number_of_minutes))
  coordinates = CoordinatesDays.objects.filter(latitude=lat, longitude=lon)
  if coordinates.exists():
    print("Coordinates Exists")
    coordinate = CoordinatesDays.objects.filter(latitude=lat, longitude=lon, time__gt=new_time)
    if coordinate.exists():
      print("Data is Relevant")
      queryset = Days.objects.filter(coordinatesDays=coordinate.first())
    else:
      data = getDays(lat, lon)
      print(coordinates)
      print("Data is not Relevant, Data is Updating")
      coordinates.update(latitude=lat, longitude=lon, time=datetime.now())
      days = data.get('daily')
      for day in days:
        dt = datetime.fromtimestamp(int(day.get('dt')))
        maxtemperature = day.get('temp').get('max')
        mintemperature = day.get('temp').get('min')
        pressure = day.get('pressure')
        humidity = day.get('humidity')
        windspeed = day.get('wind_speed')
        weather = day.get('weather')[0].get('main')
        Days.objects.filter(coordinatesDays=coordinates.first()).update(time=dt, maxtemperature=maxtemperature, mintemperature=mintemperature, pressure=pressure, humidity=humidity, windspeed=windspeed, weather=weather)
      queryset = Days.objects.filter(coordinatesDays=coordinates.first())
  else:
    print("New Data Creating")
    data = getDays(lat, lon)
    coordinates = CoordinatesDays.objects.create(latitude=lat, longitude=lon, time=datetime.now())
    print(coordinates)
    days = data.get('daily')
    for day in days:
      dt = datetime.fromtimestamp(int(day.get('dt')))
      maxtemperature = day.get('temp').get('max')
      mintemperature = day.get('temp').get('min')
      pressure = day.get('pressure')
      humidity = day.get('humidity')
      windspeed = day.get('wind_speed')
      weather = day.get('weather')[0].get('main')
      Days.objects.create(coordinatesDays=coordinates, time=dt, maxtemperature=maxtemperature, mintemperature=mintemperature, pressure=pressure, humidity=humidity, windspeed=windspeed, weather=weather)
    queryset = Days.objects.filter(coordinatesDays=coordinates)
  return queryset

def deleteData():
  current_time  = datetime.today()
  new_time = (current_time - timedelta(minutes=number_of_minutes))
  CoordinatesDays.objects.filter(time__lt=new_time).delete()
  CoordinatesMinutes.objects.filter(time__lt=new_time).delete()
  CoordinatesHourly.objects.filter(time__lt=new_time).delete()