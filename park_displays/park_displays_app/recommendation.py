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


def getScoreOnBody(score, gender,age,weight,height,avgweekkm=None):
    # score based on gender, age, bmi, avgweekkm
    if gender.lower() == "female":
        score -= 10
    if gender.lower() == "other":
        score -= 5
    if age <= 14:
        score -= 20
    if age >= 15 and age <= 18:
        score -= 10
    if age >= 19 and age <= 23:
        score -= 5
    if age >= 24 and age <= 33:
        pass
    if age >= 34 and age <= 42:
        score -= -10
    if age >= 43 and age <= 55:
        score -= 20
    if age >= 56 and age <= 67:
        score -= 25
    if age >= 68 and age >= 75:
        score -= 30
    if age >= 76:
        score -= 35
    bmi = (weight) / (height ^ 2)
    if bmi < 16:
        score -= 10
    if bmi < 18.5 and bmi >= 16:
        score -= 5
    if bmi >= 18.5 and bmi < 25:
        pass
    if bmi >= 25 and bmi < 30:
        score -= 5
    if bmi >= 30 and bmi < 35:
        score -= 10
    if bmi >= 35:
        score -= 15
    if avgweekkm!=None:
        if avgweekkm < 30:
            score -= 10
        if avgweekkm >= 30 and avgweekkm < 60:
            score -= 5
    return score
class RunWalkRecommender():
    def __init__(self,gender,age,weight,height,kcal,activity,avgweekkm,shoetype,path_types):
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
        score=getScoreOnBody(score,self.gender,self.age,self.weight,self.height,self.avgweekkm)# worst score depending on body only is 100-70=30
        score=self.getScoreOnWeather(score,weather)# worst score depending on weather only is 100-25=75
        # worst score depending on body and weather is 100-70-25=5
        pathscores=self.getPathScores(score,"running")#shoetype depending on weight and path type, and length, steepness, desired kcal
        paths_with_scores=[None]*len(self.paths)
        for i in range(len(pathscores)):
            paths_with_scores[i]=(pathscores[i],self.paths[i])
        return paths_with_scores#pathscore, path
    def recommendWalking(self,weather):
        score = 100
        score = getScoreOnBody(score,self.gender,self.age,self.weight,self.height,self.avgweekkm)  # worst score depending on body only is 100-70=30
        score = self.getScoreOnWeather(score, weather)  # worst score depending on weather only is 100-25=75
        # worst score depending on body and weather is 100-70-25=5
        pathscores = self.getPathScores(score,
                                        "walking")  # shoetype depending on weight and path type, and length, steepness, desired kcal
        paths_with_scores = [None] * len(self.paths)
        for i in range(len(pathscores)):
            paths_with_scores[i] = (pathscores[i], self.paths[i])
        return paths_with_scores  # pathscore, path

    def getScoreOnWeather(self, score,weather):
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
            score-=3
        return score

    def getPathScores(self,atleteCondition,activity):
        # shoetype depending on weight and path type, and length, steepness, desired kcal
        weightperkm=self.weight
        if atleteCondition>90:
            weightperkm=self.weight-0.2*self.weight
        if atleteCondition>80 and atleteCondition<=90:
            weightperkm = self.weight - 0.1 * self.weight
        if atleteCondition<60:
            weightperkm = self.weight + 0.2 * self.weight
        if atleteCondition<70 and atleteCondition>=60:
            weightperkm = self.weight + 0.1 * self.weight
        pathscores = [100] * len(self.paths)
        for i in range(len(self.paths)):
            if int(self.paths[i][0][2])!=0:#steepness different than 0
                weightperkm+=weightperkm*(int(self.paths[i][0][2])/100)#eg at steepness level weight=70, steepness 2% =>weight=70+70*(2/100)=70+70*0.02=70+1.4=71.4
            if self.paths[i][0][1]=="Pavement":
                weightperkm -= 0.01 * weightperkm
            if self.paths[i][0][1]=="Dirt":
                weightperkm += 0.01 * weightperkm
            if self.shoetype in ["Road A3","Trail"]:
                weightperkm+=0.01*weightperkm
            if self.shoetype in ["Road A1","Track"]:
                weightperkm-=0.01*weightperkm
            if activity=="walking":
                weightperkm*=0.40
            requiredkcal=weightperkm*(int(self.paths[i][0][3]))/1000#adjusted weight*path length in km
            pathscores[i] =(1-(abs(self.kcal - requiredkcal) / self.kcal))*100#(1-relative error)*100
        return pathscores

class GymRecommender():
    def __init__(self,gender,age,weight,height,kcal,bodyparts:[],machines:[],gymtool_scores):
        self.gender=gender
        self.age=age
        self.weight=weight
        self.height=height
        self.kcal=kcal
        self.bodyparts=bodyparts
        self.machines=machines
        self.gymtool_scores=gymtool_scores
    def recommendActivities(self):
        bodyscore=100
        bodyscore=getScoreOnBody(bodyscore,self.gender,self.age,self.weight,self.height)
        machinescores=self.getMachinesWithScores()
        machines_with_time=self.getMachinesWithTime(machinescores,bodyscore)
        return machines_with_time#list of (machine, time)

    def getMachinesWithScores(self):
        machinescores=[]
        for machine in self.machines:
            bodypartdict={}
            machinescore=None
            for gymtool in self.gymtool_scores:
                if gymtool[0]==machine[0]:
                    machinescore=gymtool
                    break
            for bodypart in self.bodyparts:
                bodypart=(bodypart.replace(" ",""))
                bodypart=bodypart.lower()
                bodypartdict[bodypart]=machinescore[1][bodypart]
            machinescores.append((machine[0],bodypartdict))
        return machinescores

    def getMachinesWithTime(self, machinescores, bodyscore):
        divider=7
        if self.weight<60:
            divider=7.5
        if self.weight>=60 and divider<75:
            divider=7
        if self.weight>=75:
            divider=6.5
        if bodyscore>90:
            divider+=0.2
        if bodyscore>80 and bodyscore<=90:
            divider += 0.3
        if bodyscore<60:
            divider -= 0.3
        if bodyscore<70 and bodyscore>=60:
            divider -= 0.2
        time=self.kcal/divider#minutes
        machinescoressum = {}
        for machinescore in machinescores:
            sumscoremachine=0
            for bodypart in machinescore[1].keys():
                sumscoremachine += int(machinescore[1][bodypart])
            machinescoressum[machinescore[0]]=sumscoremachine
        ratiosmachines={}
        totsumscore=0
        for machine in machinescoressum.keys():
            totsumscore+=machinescoressum[machine]
        for machine in machinescoressum.keys():
            ratiosmachines[machine]=machinescoressum[machine]/totsumscore
        machineswithtime={}
        for machine in ratiosmachines.keys():
            machineswithtime[machine]=time*ratiosmachines[machine]

        return machineswithtime


class FreeweightStretchingRecommender():
    def __init__(self,gender,age,weight,height,kcal,intensity, stretching=False, freeweight=False):
        self.gender=gender
        self.age=age
        self.weight=weight
        self.height=height
        self.kcal=kcal
        self.intensity=intensity#0-100
        self.stretching=stretching
        self.freeweight=freeweight
    def recommendExercises(self):
        flexs = XmlManager(os.path.dirname(os.path.realpath(
            __file__)) + os.sep + "xmldata" + os.sep + "athlete_filters.xml").getFlexibilityexericises()
        strenghts = XmlManager(os.path.dirname(
            os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "athlete_filters.xml").getStrenghtexericises()
        time=1.2*self.intensity#1.2 seconds per level of intensity, max intensity is 120 seconds per exercises
        if self.stretching and not self.freeweight:
            return [(x, time, time/2) for x in flexs]#list of (exercise, time, breaktime)
        if not self.stretching and self.freeweight:
            # http://www.fitclick.com/calories_burned
            if self.weight>=120:
                plankconsumption=3
                sideplankconsumption = 6
                squatconsumption=6
                pushupconsumption=5#per minute
            if self.weight>=95 and self.weight<120:
                plankconsumption = 2
                pushupconsumption=2
                squatconsumption = 5
                sideplankconsumption = 5
            if self.weight >= 70 and self.weight < 90:
                plankconsumption = 2
                sideplankconsumption = 4
                squatconsumption = 4
                pushupconsumption = 2
            if self.weight < 70:
                plankconsumption = 1
                sideplankconsumption=3
                squatconsumption = 3
                pushupconsumption = 2
            averageconsumption=(plankconsumption+sideplankconsumption+squatconsumption+pushupconsumption)/4
            weightplank=plankconsumption/averageconsumption
            weightsideplank = sideplankconsumption / averageconsumption
            weightsquat = squatconsumption / averageconsumption
            weightpushup = pushupconsumption / averageconsumption
            if weightplank > 1:
                weightplank = weightplank - abs(1 - weightplank) * 2
            elif weightplank < 1:
                weightplank = weightplank + abs(1 - weightplank) * 2
            if weightsideplank > 1:
                weightsideplank = weightsideplank - abs(1 - weightsideplank) * 2
            elif weightsideplank < 1:
                weightsideplank = weightsideplank + abs(1 - weightsideplank) * 2
            if weightsquat > 1:
                weightsquat = weightsquat - abs(1 - weightsquat) * 2
            elif weightsquat < 1:
                weightsquat = weightsquat + abs(1 - weightsquat) * 2
            if weightpushup > 1:
                weightpushup = weightpushup - abs(1 - weightpushup) * 2
            elif weightpushup < 1:
                weightpushup = weightpushup + abs(1 - weightpushup) * 2
            tottime=self.kcal/averageconsumption
            timeplank=((tottime/4)*weightplank)*60#seconds
            timesideplank=((tottime/4)*weightsideplank)*60
            timesquat=((tottime/4)*weightsquat)*60
            timepushup=((tottime/4)*weightpushup)*60
            repetitions = 1
            if self.intensity>=50 and self.intensity<75:
                timeplank/=2
                timesideplank/=2
                timesquat/=2
                timepushup/=2
                repetitions=2
            if self.intensity>=25 and self.intensity<50:
                timeplank /= 3
                timesideplank /= 3
                timesquat /= 3
                timepushup /= 3
                repetitions = 3
            if self.intensity<25:
                timeplank /= 4
                timesideplank /= 4
                timesquat /= 4
                timepushup /= 4
                repetitions = 4
            return [("Plank",timeplank,0.6*self.intensity,repetitions),("Side Plank",timesideplank,0.6*self.intensity,repetitions),("Squat",timesquat,0.6*self.intensity,repetitions),("Push-up",timepushup,0.6*self.intensity,repetitions)]#list of (exercise, time, breaktime,repetitions)
class GroupRecommender():
    def __init__(self,group,intensity,stretching=False, freeweight=False):
        self.group=group
        self.intensity=intensity
    def recommendExercises(self):
        return [(None,None,None)]#list of (exercise, time, breaktime)