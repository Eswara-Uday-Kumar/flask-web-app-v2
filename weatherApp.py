import json
import requests

token = "b6a83c4d78b1488bae863944231405"
baseurl = "https://api.weatherapi.com/v1/"
api = ""
location = input("Enter city name: ").capitalize()
days = int(input("Enter number of history days: "))

if days == 1:
    api = baseurl+"current.json?key="+token+"&q="+location+"&aqi=no"
elif days > 1:
    api = baseurl+"forecast.json?key="+token+"&q="+location+"&days="+str(days)+"&aqi=no&alerts=no"


print(api)

