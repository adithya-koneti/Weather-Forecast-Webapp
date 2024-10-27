from django.urls import path
from .views import weather_home,get_weather

urlpatterns = [
    path('',weather_home,name='weather_home'),
    path('weather/', get_weather, name='get_weather'),
]
