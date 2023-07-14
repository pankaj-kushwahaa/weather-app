from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('home/', views.HandleRequest.as_view(), name='request'),
  path('weather/api', views.api, name='api'),
  path('api-doc', views.apiDoc, name='api-doc'),
]
