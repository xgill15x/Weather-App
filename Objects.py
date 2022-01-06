#Author: Jason Gill

import pip._vendor.requests;

class WeatherApiConn:
    def __init__(self, myCity, myCountryCode):
        self.myCity = myCity
        self.myCountryCode = myCountryCode
        self.myApiKey = "4e6c923cb35bf9bbfd9122fcd92a31cf"
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
            'x-rapidapi-key': "769176a291mshd466531c89c2ae8p16a9c6jsn66088812c1b0"
        }

        self.originCoords = originCoords
        self.destinationCoords = destinationCoords
        self.coordPairs = {"origin": originCoords, "destination": destinationCoords}
        
        self.trafficApiResponse = pip._vendor.requests.request("GET", self.routeApi, headers=self.routeApiHeaders, params=self.coordPairs).json()