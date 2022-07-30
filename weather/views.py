from django.shortcuts import render
import requests


def index(request):
    appid = '8450022c6e5a6624d730152e02d959dc'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=" +appid
    city = 'London'
    return render(request, 'weather/index.html')
