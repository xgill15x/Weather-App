#Author: Jason Gill
#helper file

import objects;

class WeatherMessage():
    def __init__(self, mainWeather, tempHigh, tempLow, tempFeelsLike, currentTemp, needUmbrella, jacketType, trafficTime):
        self.mainWeather = mainWeather
        self.tempHigh = tempHigh
        self.tempLow = tempLow
        self.tempFeelsLike = tempFeelsLike
        self.currentTemp = currentTemp
        self.needUmbrella = needUmbrella
        self.jacketType = jacketType
        self.trafficTime = trafficTime

#Umbrella needed if rain >= .5mm/h
def isUmbrellaNeeded(weatherApiResponse):

    try:
        mmOfRainPerHour = weatherApiResponse['rain']['1h']
    except:
        return "No" 

    if (mmOfRainPerHour >= 0.5):
        return "Yes"

    return "No"

#recommends jacket type based on cold
def getJacketType(weatherApiResponse):

    tempFeelsLike = round(weatherApiResponse['main']['feels_like'])

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
def getTrafficTimeForCoordPairs(originCoords, destinationCoords):

    #routeApi call
    trafficApiConn = objects.TrafficApiConn(originCoords, destinationCoords)
    trafficApiResponse = trafficApiConn.trafficApiResponse

    rawTrafficTimeInSeconds = float(trafficApiResponse["route"]["duration"])

    trafficTimeInMinutes = round(rawTrafficTimeInSeconds/60)

    return trafficTimeInMinutes