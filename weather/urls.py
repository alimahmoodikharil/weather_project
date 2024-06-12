from django.urls import path

import .views


urlpatterns = [
    path('', views.weather_index, name='weather')
]