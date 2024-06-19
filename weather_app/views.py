from django.shortcuts import render
import requests

def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = '6bf5d25bb73b4bb5a61125216241806'
        response = requests.get(f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}')
        weather_data = response.json()

        print(weather_data)

        iconsize = weather_data['current']['condition']['icon'].replace("64x64", "128x128")
  

        context = {
            'city': city,
            'country': weather_data['location']['country'],
            'region' : weather_data['location']['region'],  
            'temperature': weather_data['current']['temp_c'],
            'temperaturef': weather_data['current']['temp_f'],
            'description': weather_data['current']['condition']['text'],
            'icon': iconsize,
            'humidity': weather_data['current']['humidity'],
            'localtime': weather_data['location']['localtime'],
        }

        return render(request, 'weather_app/index.html', context)
    else:
        return render(request, 'weather_app/index.html')
