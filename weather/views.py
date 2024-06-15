from django.shortcuts import render
import urllib.request
import json


def weather_index(request):
    if request.method == 'POST':
        city = request.POST['city']

        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='
                                         + city + '&units=metric&appid=1c3a82e67c2ee173dddfd742acc61870').read()
        list_of_data = json.loads(source)
        data = {
            'country_code': str(list_of_data['sys']['country']),
            'coordinate':   str(list_of_data['coord']['lon']) + str(list_of_data['coord']['lat']),
            'temp': str(list_of_data['main']['temp']),
            'pressure': str(list_of_data['main']['pressure']),
            'humidity': str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon']
        }
    else:
        data = {}


    return render(request, 'weather/weather_index.html', data)
