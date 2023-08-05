import requests, json
# from bs4 import BeautifulSoup

user_input = input('Enter you location : ')
params = {
    "key" : "d277285a197f4a7fa56123639230508",
    "q" : user_input.capitalize(),
}
r = requests.get("https://api.weatherapi.com/v1/forecast.json", params=params)
response = str(r.content)
response = response.replace('b','')
response = response.replace("'",'')
response =  json.loads(response)
print(response)
temp_in_c = response['current']['temp_c']
temp_in_f = response['current']['temp_f']
is_day = str(response['current']['is_day'])
if is_day == "1":
    is_day = "Day"
else:
    is_day = "Night"

print(f"Forcast Details of {response['location']['name']} located in {response['location']['country']} country.")
print(f"{response['location']['name']} Longitude : {response['location']['lon']}")
print(f"{response['location']['name']} Latitude : {response['location']['lat']}")
print(f"{response['location']['name']} Time Right Now : {response['location']['localtime']}")
print(f"{response['location']['name']} Night or Day? : {is_day}")
print(f"{response['location']['name']} Temperature in Celcius : ", temp_in_c)
print(f"{response['location']['name']} Temperature in Fahrenheit : ", temp_in_f)
print(f"{response['location']['name']} Condition : {response['current']['condition']['text']}")
print(f"{response['location']['name']} Wind : {response['current']['wind_mph']} mph or {response['current']['wind_kph']} kph")
print(f"{response['location']['name']} Humidity : {response['current']['humidity']}")
print(f"{response['location']['name']} Wind Degree : {response['current']['wind_degree']}")
print(f"{response['location']['name']} Wind Pressure : {response['current']['pressure_mb']} mb")
print(f"{response['location']['name']} Cloud : {response['current']['cloud']}")
print(f"{response['location']['name']} Chance of snow? : {response['current']['chance_of_snow']}")
print(f"{response['location']['name']} Chance of Rain? : {response['current']['will_it_rain']}")
print(f"{response['location']['name']} Gust : {response['current']['chance_of_snow']} mph")