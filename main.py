import requests

print("Input the name of the city: ")
city = input()

base_url = "http://api.openweathermap.org/data/2.5/weather?"
api_key = "b96838007ab21153be4019a78056bc8e"

url = base_url + "appid=" + api_key + "&q=" + city

response = requests.get(url).json()

print("weather right now: ", response.get('weather')[0].get('description'))
print("temperature in Kelvins: ", response.get('main').get('temp'))
print("pressure: ", response.get('main').get('pressure'))
print("wind speed: ", response.get('wind').get('speed'))
print(response)