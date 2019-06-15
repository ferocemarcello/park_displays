import os

from .data_manager import ParkManager
from .xmlmanager import XmlManager
from .weather import Weather
from datetime import  datetime
import pytz
APPID="676536c0f3533a7868a16beed9f14ba4"
kelvin_zero_celsius=273.15
#https://openweathermap.org/weather-conditions
weatherdescthunderstorm={200:"thunderstorm with light rain",201:"thunderstorm with rain",202:"thunderstorm with heavy rain",210:"light thunderstorm",211:"thunderstorm",212:"heavy thunderstorm",221:"ragged thunderstorm",230:"thunderstorm with light drizzle",231:"thunderstorm with drizzle",232:"thunderstorm with heavy drizzle"}
weatherdescdrizzle={300:"light intensity drizzle",301:"drizzle",302:"heavy intensity drizzle",310:"light intensity drizzle rain",311:"drizzle rain",312:"heavy intensity drizzle rain",313:"shower rain and drizzle",314:"heavy shower rain and drizzle",321:"shower drizzle"}
weatherdescrain={500:"light rain",501:"moderate rain",502:"heavy intensity rain",503:"very heavy rain",504:"extreme rain",511:"freezing rain",520:"light intensity shower rain",521:"shower rain",522:"heavy intensity shower rain",531:"ragged shower rain"}
weatherdescsnow={600:"light snow",601:"Snow",602:"Heavy snow",611:"Sleet",612:"Light shower sleet",613:"Shower sleet",615:"Light rain and snow",616:"Rain and snow",620:"Light shower snow",621:"Shower snow",622:"Heavy shower snow"}
weatherdescatmosphere={701:"mist",711:"Smoke",721:"Haze",731:"sand/ dust whirls",741:"fog",751:"sand",761:"dust",762:"volcanic ash",771:"squalls",781:"tornado"}
weatherdescclear={800:"clear sky"}
weatherdescclouds={801:"few clouds: 11-25%",802:"scattered clouds: 25-50%",803:"scattered clouds: 25-50%",804:"overcast clouds: 85-100%"}
class RunWalkRecommender():
    def __init__(self,path_types,gender,age,weight,height,kcal,avgweekkm,shoetype,activity,):
        self.gender=gender
        self.age=age
        self.weight=weight
        self.height=height
        self.kcal=kcal
        self.avgweekkm=avgweekkm
        self.activity=activity
        xmg=(XmlManager(os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "park_data.xml"))
        self.paths=ParkManager(parkname="englischer_garten",xmlmanager=xmg,pathtypes=path_types).getPaths()
        self.shoetype=shoetype
    def recommendPaths(self):
        tz = pytz.timezone('Europe/Berlin')
        berlin_now = datetime.now(tz)
        hour = berlin_now.hour
        minute = berlin_now.minute
        weather=Weather("Munich",APPID)
        if self.activity=='running':
            return self.recommendRunning(weather)
        else:
            return self.recommendWalking(weather)
    def recommendRunning(self,weather):
        score=100
        #score based on gender, age, bmi, avgweekkm
        if self.gender.lower()=="female":
            score-=10
        if self.gender.lower()=="other":
            score-=5
        if self.age<=14:
            score-=20
        if self.age>=15 and self.age<=18:
            score-=10
        if self.age>=19 and self.age<=23:
            score -= 5
        if self.age>=24 and self.age<=33:
            pass
        if self.age>=34 and self.age<=42:
            score -= -10
        if self.age>=43 and self.age<=55:
            score-=20
        if self.age>=56 and self.age<=67:
            score-=25
        if self.age>=68 and self.age>=75:
            score-=30
        if self.age>=76:
            score-=35
        bmi=(self.weight)/(self.height^2)
        if bmi<16:
            score-=10
        if bmi<18.5 and bmi >=16:
            score-=5
        if bmi>=18.5 and bmi<25:
            pass
        if bmi>=25 and bmi<30:
            score -= 5
        if bmi>=30 and bmi<35:
            score-=10
        if bmi >=35:
            score-=15
        if self.avgweekkm<30:
            score-=10
        if self.avgweekkm>=30 and self.avgweekkm<60:
            score-=5
        if weather.desc["id"] in weatherdescthunderstorm.keys() or weather.desc["id"] in weatherdescsnow.keys():
            score-=5
        if weather.temp<5+kelvin_zero_celsius or weather.temp>25+kelvin_zero_celsius:
            score -= 2
        if weather.temp<0+kelvin_zero_celsius or weather.temp>30+kelvin_zero_celsius:
            score -= 3
        if weather.hum>80 and weather.hum<=90:
            score -= 2
        if weather.hum>90:
            score-=3
        if weather.wind_speed>=10:
            score-=2
        if weather.wind_speed>=17:
            score-=3
        if weather.pres<=920:
            score-=2
        if weather.pres<=870:
            score-3
        #shoetype depending on weight and path type, and length
        #shoetype/pathtype-length
        return [(None,None,None,None)]#pathid,#warmup,#cooldown,#avgspeed
    def recommendWalking(self):
        return [(None,None,None,None)]#pathid,#warmup,#cooldown,#avgspeed. warmup and cooldown will have 0 value. They are not necessary for walking
class GymRecommender():
    def __init__(self,gender,age,weight,height,kcal,bodyparts:[]):
        self.gender=gender
        self.age=age
        self.weight=weight
        self.height=height
        self.kcal=kcal
        self.bodyparts=bodyparts
    def recommendActivities(self):
        return [(None,None,None)]#list of (machine, time, intensity)   intensity can be speed, weight, Force...
class FreeweightStretchingRecommender():
    def __init__(self,gender,age,weight,height,kcal,intensity, stretching=False, freeweight=False):
        self.gender=gender
        self.age=age
        self.weight=weight
        self.height=height
        self.kcal=kcal
        self.intensity=intensity
    def recommendExercises(self):
        return [(None,None,None)]#list of (exercise, time, breaktime)
class GroupRecommender():
    def __init__(self,group,intensity,stretching=False, freeweight=False):
        self.group=group
        self.intensity=intensity
    def recommendExercises(self):
        return [(None,None,None)]#list of (exercise, time, breaktime)