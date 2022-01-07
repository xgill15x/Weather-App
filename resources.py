#Author: Jason Gill
#Contains api calls

import pip._vendor.requests;
import privateInfo

class WeatherApiConn:
    def __init__(self, myCity, myCountryCode):
        self.myCity = myCity
        self.myCountryCode = myCountryCode
        self.myApiKey = privateInfo.weatherApiKey
        self.weatherApiEndpoint = "https://api.openweathermap.org/data/2.5/weather?q=" + self.myCity + "," + self.myCountryCode + "&appid=" + self.myApiKey + "&units=metric"
        self.weatherApiResponse = pip._vendor.requests.get(self.weatherApiEndpoint).json()
    
    def getMainWeather(self):
        return self.weatherApiResponse['weather'][0]['main']

    def getCurrentTemp(self):
        return round(self.weatherApiResponse['main']['temp'])

    def getTempFeelsLike(self):
        return round(self.weatherApiResponse['main']['feels_like'])

    def getTempHigh(self):
        return round(self.weatherApiResponse['main']['temp_max'])

    def getTempLow(self):
        return round(self.weatherApiResponse['main']['temp_min'])

class TrafficApiConn:
    def __init__(self, originCoords, destinationCoords):
        
        self.routeApi = "https://trueway-directions2.p.rapidapi.com/FindDrivingPath"
        self.routeApiHeaders = {
            'x-rapidapi-host': "trueway-directions2.p.rapidapi.com",
            'x-rapidapi-key': privateInfo.rapidApiKey
        }

        self.originCoords = originCoords
        self.destinationCoords = destinationCoords
        self.coordPairs = {"origin": originCoords, "destination": destinationCoords}
        
        self.trafficApiResponse = pip._vendor.requests.request("GET", self.routeApi, headers=self.routeApiHeaders, params=self.coordPairs).json()