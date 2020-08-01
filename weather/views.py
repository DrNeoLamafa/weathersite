import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
def index(request):
    appid = 'c0b99ce1c915619c10d05beddb029160'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    
    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()
    
    form = CityForm()

    

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()

        city_info = {
            
            'city': city.name,
            'temp': round(res["main"]["temp"]),
            'icon': res["weather"][0]["icon"]
        

        }
        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form }

    return render(request, 'weather/index.html', context)