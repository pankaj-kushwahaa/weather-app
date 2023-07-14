import requests
import json
# from pprint import pprint

# url = https://api.openweathermap.org/data/2.5/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={API key}
# exclude = current, minutely, hourly, daily, alerts
URL = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude={}&units=metric&appid=49cc8c821cd2aff9af04c9f98c36eb74'

headers = {
  "Content-Type" : "application/json; charset:utf-8",
  "Accept" : "application/json; indent=4"
}

def getMinutes(lat, lon):
  url = URL.format(lat, lon, 'current,hourly,daily')
  response = requests.get(url, headers=headers)
  return json.loads(response.text)

def getHours(lat, lon):
  url = URL.format(lat, lon, 'current,minutely,daily')
  response = requests.get(url, headers=headers)
  return json.loads(response.text)

def getDays(lat, lon):
  url = URL.format(lat, lon, 'current,minutely,hourly')
  response = requests.get(url, headers=headers)
  return json.loads(response.text)

# getMinutes(30.5685, 70.2595)