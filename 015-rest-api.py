import requests
import datetime
import pprint

url = 'http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b1b15e88fa797225412429c1c50c122a1'

response = requests.get(url)

data = response.json()

pprint.pprint(data)

'''
+ ausgabe  nur der Temperatur in Grad Celsius
'''

print(datetime.datetime.fromtimestamp(data['dt']))
print("%.2f Grad C" % ( data['main']['temp']-273.15 )) 

print(data['weather'][0]['main'])