#Author: Jason Gill
#DateCreated: 2022/01/03
#WeatherAppWithMotivationalQuotes

import pip._vendor.requests, json;

myApiKey = "4e6c923cb35bf9bbfd9122fcd92a31cf"
city = "surrey"
countryCode = "ca"

weatherApiEndpoint = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "," + countryCode + "&appid=" + myApiKey

weatherApiResponse = pip._vendor.requests.get(weatherApiEndpoint).json()

weather = weatherApiResponse['weather'][0]

print(weatherApiResponse)
print(weatherApiResponse['coord']['lon'])
