from ast import Dict
from http.client import HTTPResponse
from django.shortcuts import render
import requests
from .models import Weather
#import urllib.request
import json
def tweets(request):
    if request.method == 'POST':
        try:
            city = request.POST.get('city')
        except:
            city = 'mumbai'
        url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=imperial&appid=4658bfb56b16b2c80fe78f906a229555"


    #querystring = {
        #"user_id":"96479162" }
        response = requests.request('GET',url)
        l = response.json()             #converting the fetched data in json form
        #print(response.text)
        context = {                                     #creating a dictionary to store the data and pass it to template
            'city' : city,
            'pressure': str(l['main']['pressure']),
            'temperature' : str(l['main']['temp']) + 'k',
            'humidity':str(l['main']['humidity']),
            
        }
            
        t = str(l['main']['temp'])                          #saving the collected data from api to variables
        p= str(l['main']['pressure'])  
        h= str(l['main']['humidity'])
        report= Weather(place =city , temperature= t,pressure =p,humidity=h)  #passing the collected data to model -Weather
        report.save()

    else:  
        context = {} 
    
    return render(request, 'index.html', context)
    
def new(request):
    if request.method == 'POST':
        try:
            c = request.POST.get('c')
        except:
            c = 'Mumbai'
        
        pressure = Weather.objects.filter(place = c)
        temperature = Weather.objects.filter(place= c)
        humidity = Weather.objects.filter(place =c)
        content = {
            'place' : c,
            'temp' : temperature,
            'p':pressure,
            'h':humidity,

         }
        
    else:  
        content = {}
    
    return render(request, 'home.html', content)
        
    

    
    