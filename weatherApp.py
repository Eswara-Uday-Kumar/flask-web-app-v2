import json
import requests
import pandas as pd

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

res = requests.get(api)
response = res.json()
# for one day #print("Temperature: ", response['current']['temp_c'], "Feels Like: ", response['current']['feelslike_c'])
# for one day #print("Condition: ",response['current']['condition']['text'])

#print(response)
dates, max_temp, min_temp, avg_temp, conditions =  ([] for i in range(5))

for i in range(0, days):
    #print(response['forecast']['forecastday'][i]['date'], response['forecast']['forecastday'][i]['day']['maxtemp_c'], response['forecast']['forecastday'][i]['day']['mintemp_c'], response['forecast']['forecastday'][i]['day']['avgtemp_c'], response['forecast']['forecastday'][i]['day']['condition']['text'])
    dates.append(response['forecast']['forecastday'][i]['date'])
    max_temp.append(response['forecast']['forecastday'][i]['day']['maxtemp_c'])
    min_temp.append(response['forecast']['forecastday'][i]['day']['mintemp_c'])
    avg_temp.append(response['forecast']['forecastday'][i]['day']['avgtemp_c'])
    conditions.append(response['forecast']['forecastday'][i]['day']['condition']['text'])


data = {
    'Date': dates,
    'max_temp': max_temp,
    'min_temp': min_temp,
    'avg_temp': avg_temp,
    'condition_txt': conditions
}

df = pd.DataFrame(data)

print(df)

#for i in response['forecast']:
#    print(i)