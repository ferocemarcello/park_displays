import requests
from datetime import  datetime
class Weather():
    def __init__(self,city,appid):
        # https://openweathermap.org/current
        weather = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&APPID=' + appid)
        prweather = (weather.json())
        self.desc = (prweather['weather'])[0]
        self.hum = (prweather['main'])["humidity"]
        self.temp = (prweather['main'])['temp']  # kelvin
        self.visibility = prweather['visibility']  # meters
        self.pres = (prweather['main'])['pressure']  # hpa
        self.wind_speed = (prweather['wind'])['speed']  # m/s
        self.clouds = prweather['clouds']  # %cloudiness
        self.sunrise = datetime.fromtimestamp(prweather['sys']['sunrise'])  # ,tz
        self.sunset = datetime.fromtimestamp(prweather['sys']['sunset'])
        self.pastrain = None
        try:
            pastrain = prweather['rain']
        except:
            pass