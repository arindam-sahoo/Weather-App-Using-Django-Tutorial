import requests
from django.shortcuts import render
import os
import dotenv
from .forms import CityForm

def get_weather(city_name):
    dotenv.load_dotenv()

    api_key = os.getenv("API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    weather_data = {
        "city": city_name,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
    }

    return weather_data

def weather(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['city']
            weather_data = get_weather(city_name)
    else:
        form = CityForm()
        weather_data = None

    context = {'form': form, 'weather_data': weather_data}
    return render(request, 'weather_app/weather.html', context)
