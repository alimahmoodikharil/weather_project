from django.shortcuts import render
from urllib import request


def weather_index(request):
    return render(request, 'weather/weather_index', data)
