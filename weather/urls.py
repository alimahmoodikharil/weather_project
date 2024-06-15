from django.urls import path

from .views import weather_index


urlpatterns = [
    path('', weather_index, name='weather'),
]