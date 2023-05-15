import json
import requests
import pandas as pd

#current = "provides weather details today"
#forecast = "Number of days of weather forecast. Value ranges from 1 to 10"
#history = "provides weather details for previous days"
#Future = "provides weather details for Dates between 14 days and 300 days from today in the future in yyyy-MM-dd format"


token = "b6a83c4d78b1488bae863944231405"
baseurl = "https://api.weatherapi.com/v1/"
api = ""
choice = input("select options Current or Forecast or History: ").lower()
location = input("Enter city name: ").capitalize()


if choice == 'current':
    pass
elif choice == 'forecast':
    days = int(input("Enter number of days: "))
elif choice == 'history' or choice == 'future':
    date = input("Enter date in yyyy-mm-dd format")


if choice == 'current':
    api = baseurl+"current.json?key="+token+"&q="+location+"&aqi=no"
elif choice == 'forecast':
    api = baseurl+"forecast.json?key="+token+"&q="+location+"&days="+str(days)+"&aqi=no&alerts=no"
elif choice == 'history':
    api = baseurl+"history.json?key="+token+"&q="+location+"&dt="+date

print(api)

res = requests.get(api)
response = res.json()

#Current
# for one day #print("Temperature: ", response['current']['temp_c'], "Feels Like: ", response['current']['feelslike_c'])
# for one day #print("Condition: ",response['current']['condition']['text'])

# print(response)

# Forecast or History or Future will be in same format starting with forecast
dates, max_temp, min_temp, avg_temp, conditions = ([] for i in range(5))

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

# for i in response['forecast']:
#    print(i)
