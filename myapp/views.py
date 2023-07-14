from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.core.serializers import serialize
from .service import checkMinutesAndSave, checkDaysAndSave, checkHourAndSave, deleteData
import json

def home(request):
  deleteData()
  return render(request, 'myapp/home.html')

class HandleRequest(View):
  def get(self, request):
    return render(request, 'myapp/home.html')
  
  def post(self, request):
    detailing = request.POST.get('detailing-type').strip()
    latitude = request.POST.get('latitude').strip()
    longitude = request.POST.get('longitude').strip()
    if detailing == 'minutes':
      queryset = checkMinutesAndSave(latitude, longitude)
      data = dict(minutes=queryset, lat=latitude, lon=longitude, de=detailing)
      return render(request, 'myapp/minutes.html', data)
    elif detailing == 'hours':
      queryset = checkHourAndSave(latitude, longitude)
      data = dict(hours=queryset, lat=latitude, lon=longitude, det=detailing)
      return render(request, 'myapp/hourly.html', data)
    elif detailing == '7days':
      queryset = checkDaysAndSave(latitude, longitude)
      data = dict(days=queryset, lat=latitude, lon=longitude, det=detailing)
      return render(request, 'myapp/days.html', data)

def apiDoc(request):
  data = dict(url=request.build_absolute_uri("/"))
  return render(request, 'myapp/api-doc.html', data)

def api(request):
  try:
    detailing = request.GET.get('detailing-type')
    latitude = request.GET.get('lat')
    longitude = request.GET.get('lon')
    if detailing is not None and latitude is not None and longitude is not None: 
      if detailing == 'minutely':
        queryset = checkMinutesAndSave(latitude, longitude)
        serialized_data = serialize("json", queryset, fields=('time', 'precipitate'))
        data = json.loads(serialized_data)
        for d in data:
          del d['pk']
          del d['model']
        return JsonResponse(data, safe=False, status=200)
      elif detailing == 'hourly':
        queryset = checkHourAndSave(latitude, longitude)
        serialized_data = serialize("json", queryset, fields=('time', 'temperature', 'pressure', 'humidity', 'windspeed', 'weather'))
        data = json.loads(serialized_data)
        for d in data:
          del d['pk']
          del d['model']
        return JsonResponse(data, safe=False, status=200)
      elif detailing == 'daily':
        queryset = checkDaysAndSave(latitude, longitude)
        serialized_data = serialize("json", queryset, fields=('time', 'maxtemperature', 'mintemperature', 'pressure', 'humidity', 'windspeed', 'weather'))
        data = json.loads(serialized_data)
        for d in data:
          del d['pk']
          del d['model']
        return JsonResponse(data, safe=False, status=200)
      else:
        return HttpResponse(json.dumps(dict(msg='Something went wrong, request is not valid')), content_type="application/json", status=404)
    else:
      return HttpResponse(json.dumps(dict(msg='All fields are required')), content_type="application/json", status=404)
  except:
    return HttpResponse(json.dumps(dict(msg='All fields are required')), content_type="application/json", status=404)