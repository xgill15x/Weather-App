#Author: Jason Gill
#DateCreated: 2022/01/03
#WeatherAppWithMotivationalQuotes

import Objects, helpers;

#origin and destination coords defined here (for traffic)       #testCoords: "origin":"40.629041,-74.025606","destination":"40.627177,-73.980853"
originCoords = "49.16721382662555, -122.8723728872053"
destinationCoords = "49.27819541642316, -122.91989418296538"

#location info (for weather)
myCity = "surrey"
myCountryCode = "ca"

weatherApiConn = Objects.WeatherApiConn(myCity, myCountryCode)

#Initializing text components
weather = weatherApiConn.getMainWeather()
tempHigh = weatherApiConn.getTempHigh()
tempLow = weatherApiConn.getTempLow()
tempFeelsLike = weatherApiConn.getTempFeelsLike()
currentTemp = weatherApiConn.getCurrentTemp()
needUmbrella = helpers.isUmbrellaNeeded(weatherApiConn.weatherApiResponse)
jacketType = helpers.getJacketType(weatherApiConn.weatherApiResponse)
trafficTime = helpers.getTrafficTimeForCoordPairs(originCoords, destinationCoords)


####### Home #######

#Constructing message instance
myWeatherMessage = Objects.WeatherMessage(weather, tempHigh, tempLow, tempFeelsLike, currentTemp, needUmbrella, jacketType, trafficTime)

print(myWeatherMessage.mainWeather)
print(myWeatherMessage.jacketType)
print("Traffic Time", myWeatherMessage.trafficTime)

print("\n")
