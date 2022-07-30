from django.shortcuts import render
import requests


def index(request):
    appid = '8450022c6e5a6624d730152e02d959dc'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" +appid
    city = 'London'
    res = requests.get(url.format(city))
    print(res.text)
    return render(request, 'weather/index.html')
