#Author: Jason Gill
#DateCreated: 2022/01/03
#WeatherAppWithTrafficTime

import objects, helpers, privateInfo

weatherApiConn = objects.WeatherApiConn(privateInfo.myCity, privateInfo.myCountryCode)

#Initializing text components
weather = weatherApiConn.getMainWeather()
tempHigh = weatherApiConn.getTempHigh()
tempLow = weatherApiConn.getTempLow()
tempFeelsLike = weatherApiConn.getTempFeelsLike()
currentTemp = weatherApiConn.getCurrentTemp()
needUmbrella = helpers.isUmbrellaNeeded(weatherApiConn.weatherApiResponse)
jacketType = helpers.getJacketType(weatherApiConn.weatherApiResponse)
trafficTime = helpers.getTrafficTimeForCoordPairs(privateInfo.originCoords, privateInfo.destinationCoords)

#Constructing message instance
myWeatherComponents = helpers.WeatherComponents(weather, tempHigh, tempLow, tempFeelsLike, currentTemp, needUmbrella, jacketType, trafficTime)
myWeatherMessage = helpers.createWeatherMessage(myWeatherComponents)

#send message
helpers.sendSmsMessage(myWeatherMessage)


print("Program Finished.")