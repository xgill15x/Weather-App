#Author: Jason Gill
#DateCreated: 2022/01/03
#WeatherAppWithMotivationalQuotes

import pip._vendor.requests, json;

#origin and destination coords defined here
originCoords = "49.16721382662555, -122.8723728872053"
destinationCoords = "49.27819541642316, -122.91989418296538"

#testCoords
#"origin":"40.629041,-74.025606","destination":"40.627177,-73.980853"

class createWeatherMessage():
    def __init__(self, mainWeather, tempHigh, tempLow, tempFeelsLike, currentTemp):
        self.mainWeather = mainWeather
        self.tempHigh = tempHigh
        self.tempLow = tempLow
        self.tempFeelsLike = tempFeelsLike
        self.currentTemp = currentTemp
        self.needUmbrella = None
        self.jacketType = None
        self.trafficTime = None

#routeApi setup
routeApi = "https://trueway-directions2.p.rapidapi.com/FindDrivingPath"
coordPairs = {"origin":originCoords,"destination":destinationCoords}
routeApiHeaders = {
    'x-rapidapi-host': "trueway-directions2.p.rapidapi.com",
    'x-rapidapi-key': "769176a291mshd466531c89c2ae8p16a9c6jsn66088812c1b0"
}

#routeApi call
trafficData = pip._vendor.requests.request("GET", routeApi, headers=routeApiHeaders, params=coordPairs).json()

#weatherApi setup
myApiKey = "4e6c923cb35bf9bbfd9122fcd92a31cf"
city = "surrey"
countryCode = "ca"

#Making call to weatherApi
weatherApiEndpoint = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "," + countryCode + "&appid=" + myApiKey + "&units=metric"
weatherApiResponse = pip._vendor.requests.get(weatherApiEndpoint).json()

#Sifting through weatherApi response
weather = weatherApiResponse['weather'][0]['main']
tempHigh = round(weatherApiResponse['main']['temp_max'])
tempLow = round(weatherApiResponse['main']['temp_min'])
tempFeelsLike = round(weatherApiResponse['main']['feels_like'])
currentTemp = round(weatherApiResponse['main']['temp'])

#Umbrella needed if rain >= .5mm/h
def isUmbrellaNeeded():

    try:
        mmOfRainPerHour = weatherApiResponse['rain']['1h']
    except:
        return "No" 

    if (mmOfRainPerHour >= 0.5):
        return "Yes"

    return "No"

#get jacket type needed accounting for cold
def getJacketType():
    if (tempFeelsLike <= 4):
        return "Heavy Jacket"

    elif (tempFeelsLike >= 5 and tempFeelsLike <= 14):
        return "Regular Jacket"
    
    elif (tempFeelsLike >= 15 and tempFeelsLike <= 23):
        return "Light Jacket"
    
    elif (tempFeelsLike > 24):
        return "No Jacket Needed"
    else:
        return "error"

#finds traffic time between 2 coords (minutes)
def getTrafficTimeForCoordPairs():

    rawTrafficTimeInSeconds = float(trafficData["route"]["duration"])

    trafficTimeInMinutes = round(rawTrafficTimeInSeconds/60)

    return trafficTimeInMinutes


####### Home #######

#My Weather message instance
myWeatherMessage = createWeatherMessage(weather, tempHigh, tempLow, tempFeelsLike, currentTemp)

#setting required fields
myWeatherMessage.needUmbrella = isUmbrellaNeeded()
myWeatherMessage.jacketType = getJacketType()
myWeatherMessage.trafficTime = getTrafficTimeForCoordPairs()

print(myWeatherMessage.mainWeather)
print(myWeatherMessage.jacketType)
print("Traffic Time", myWeatherMessage.trafficTime)

print("\n")
