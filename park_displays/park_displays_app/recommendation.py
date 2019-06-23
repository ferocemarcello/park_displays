import os

from .data_manager import ParkManager
from .xmlmanager import XmlManager
from .weather import Weather
from datetime import  datetime
import pytz
WEATHERAPPID= "676536c0f3533a7868a16beed9f14ba4"
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
    elif gender.lower() == "other":
        score -= 5
    if age <= 14:
        score -= 20
    elif 15<=age <= 18:
        score -= 10
    elif 19<=age <= 23:
        score -= 5
    elif 24<=age <= 33:
        pass#perfect age for physical activity
    elif 34<=age <= 42:
        score -= -10
    elif 43<=age<= 55:
        score -= 20
    elif 56<= age <= 67:
        score -= 25
    elif 68<= age<=75:
        score -= 30
    elif age >= 76:
        score -= 35
    bmi = (weight) / (height ^ 2)
    if bmi < 16:
        score -= 10
    elif 16<= bmi < 18.5:
        score -= 5
    elif 18.5<=bmi < 25:
        pass#perfect bmi
    elif 25<=bmi < 30:
        score -= 5
    elif 30<= bmi < 35:
        score -= 10
    elif bmi >= 35:
        score -= 15
    if avgweekkm!=None:
        if avgweekkm < 30:
            score -= 10
        elif 30<=avgweekkm < 60:
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
        #berlin_now = datetime.now(tz)
        #hour = berlin_now.hour
        #minute = berlin_now.minute
        weather=Weather("Munich", WEATHERAPPID)
        if self.activity=='running':
            return self.recommendRunning(weather)
        else:
            return self.recommendWalking(weather)
    def recommendRunning(self,weather):
        score=getScoreOnBody(score=100,gender=self.gender,age=self.age,weight=self.weight,height=self.height,avgweekkm=self.avgweekkm)# worst score depending on body only is 100-70=30
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
        elif weather.temp<0+kelvin_zero_celsius or weather.temp>30+kelvin_zero_celsius:
            score -= 3
        if 80<weather.hum<=90:
            score -= 2
        elif weather.hum>90:
            score-=3
        if weather.wind_speed>=10:
            score-=2
        elif weather.wind_speed>=17:
            score-=3
        if weather.pres<=920:
            score-=2
        elif weather.pres<=870:
            score-=3
        return score
    def getPathScores(self,atleteCondition,activity):
        # shoetype depending on weight and path type, and length, steepness, desired kcal
        weightperkm=self.weight
        if atleteCondition>90:
            weightperkm-=0.2*self.weight
        elif 80<atleteCondition<=90:
            weightperkm -=0.1 * self.weight
        elif atleteCondition<60:
            weightperkm +=0.2 * self.weight
        elif 60<=atleteCondition<70:
            weightperkm+= 0.1 * self.weight
        pathscores = [100] * len(self.paths)#every score path is up to 100
        for i in range(len(self.paths)):
            if int(self.paths[i][0][2])!=0:#steepness different than 0
                weightperkm+=weightperkm*(int(self.paths[i][0][2])/100)#eg at steepness level weight=70, steepness 2% =>weight=70+70*(2/100)=70+70*0.02=70+1.4=71.4
            if self.paths[i][0][1]=="Pavement":
                weightperkm -= 0.01 * weightperkm
            elif self.paths[i][0][1]=="Dirt":
                weightperkm += 0.01 * weightperkm
            if self.shoetype in ["Road A3","Trail"]:
                weightperkm+=0.01*weightperkm
            elif self.shoetype in ["Road A1","Track"]:
                weightperkm-=0.01*weightperkm
            if activity.lower()=="walking":
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
        bodyscore=getScoreOnBody(score=100,gender=self.gender,age=self.age,weight=self.weight,height=self.height)
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
        kcalminute=self.getKcalMin()
        kcalminute=self.adjustKcalMinBodyScore(bodyscore=bodyscore,kcalminute=kcalminute)
        time=self.kcal/kcalminute#minutes
        machinescoressum = {}
        for machinescore in machinescores:
            sumscoremachine=0
            for bodypart in machinescore[1].keys():
                sumscoremachine += int(machinescore[1][bodypart])
            machinescoressum[machinescore[0]]=sumscoremachine
        ratiosmachines={}
        totsumscore=sum([machinescoressum[key] for key in machinescoressum.keys()])
        for machine in machinescoressum.keys():
            ratiosmachines[machine]=machinescoressum[machine]/totsumscore
        machineswithtime={}
        for machine in ratiosmachines.keys():
            machineswithtime[machine]=time*ratiosmachines[machine]

        return machineswithtime
    def getKcalMin(self):#light people burn less kcal per minute
        if self.weight<60:
            return  6.5
        elif 60<=self.weight<75:
            return 7
        return 7.5
    def adjustKcalMinBodyScore(self, bodyscore, kcalminute):
        if bodyscore>90:
            return  kcalminute+ 0.2
        elif 80<bodyscore<=90:
            return kcalminute + 0.3
        elif bodyscore<60:
            return kcalminute - 0.3
        elif 60<=bodyscore<70:
            return kcalminute -0.2
        return kcalminute

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
        time=1.2*self.intensity#1.2 seconds per level of intensity, max intensity is 120 seconds per exercises
        exerciselist=[]#stretching/strenght
        bodyscore = getScoreOnBody(100, self.gender, self.age, self.weight, self.height)
        self.weight=self.adjustWeightFreeWeightBodyScore(bodyscore=bodyscore)
        time = self.adjustTimeFreeWeightBodyScore(bodyscore=bodyscore, time=time)
        if self.stretching:
            exerciselist.append([(x, time, time/2) for x in flexs])#list of (exercise, time, breaktime)
        if self.freeweight:
            strenghts = XmlManager(os.path.dirname(
                os.path.realpath(
                    __file__)) + os.sep + "xmldata" + os.sep + "athlete_filters.xml").getStrenghtexericisesKcalIntervals()
            exercises=[x[0] for x in strenghts]
            exerciseconsumptions=[]
            for ex in exercises:
                exerciseconsumptions.append(self.getExerciseConsumptionWeight(exerciseskcals=strenghts,exercise=ex))
            averageconsumption=sum(exerciseconsumptions)/len(exerciseconsumptions)
            exerciseweights=[]
            for ex in exerciseconsumptions:
                exweight=ex/averageconsumption
                if exweight > 1:
                    exweight= exweight - abs(1 - exweight) * 2
                elif exweight< 1:
                    exweight = exweight + abs(1 - exweight) * 2
                exerciseweights.append(exweight)
            tottime=self.kcal/averageconsumption#in minutes
            times=[]
            for exweight in exerciseweights:
                times.append(((tottime/len(exerciseweights))*exweight)*60)#seconds
            repetitions = 1
            if 50<=self.intensity<75:
                for i in range(len(times)):
                    times[i]/=2
                repetitions=2
            elif 25<=self.intensity<50:
                for i in range(len(times)):
                    times[i]/=3
                repetitions=3
            elif self.intensity<25:
                for i in range(len(times)):
                    times[i]/=4
                repetitions=4
            for i in range(len(exercises)):
                #60 seconds break for intensity=100=maxvalue
                exerciselist.append((exercises[i],times[i],0.6*self.intensity,repetitions))#list of (exercise, time, breaktime,repetitions)
        return tuple(exerciselist)
    def adjustWeightFreeWeightBodyScore(self, bodyscore):
        if bodyscore > 90:
            return self.weight * 0.8
        elif 80<bodyscore <= 90:
            return self.weight * 0.9
        elif 60<=bodyscore < 70:
            return self.weight* 1.2
        elif bodyscore < 60:
            return self.weight *1.1
        return self.weight
    def adjustTimeFreeWeightBodyScore(self, bodyscore, time):
        if bodyscore > 90:
            return time*1.2
        elif 80<bodyscore <= 90:
            return time*1.1
        elif 60<=bodyscore < 70:
            return time*0.8
        elif bodyscore < 60:
            return time*0.9
        return time
    def getExerciseConsumptionWeight(self, exerciseskcals, exercise):
        for i in range(len(exerciseskcals)):
            if exerciseskcals[i][0]==exercise:
                for j in range(len(exerciseskcals[i][1])):
                    if exerciseskcals[i][1][j][1]<=self.weight<exerciseskcals[i][1][j][0]:
                        return exerciseskcals[i][1][j][2]

class GroupRecommender():
    def __init__(self,numcomponents, nummales, numunder18, numover70, avgage,minage,maxage,kcal,intensity,stretching=False, freeweight=False):
        self.numcomponents=numcomponents
        self.nummales=nummales
        self.numunder18=numunder18
        self.numover70=numover70
        self.avgage=avgage
        self.minage=minage
        self.maxage=maxage
        self.kcal=kcal
        self.intensity=intensity#0-100
        self.stretching=stretching
        self.freeweight=freeweight
    def recommendExercises(self):
        groupscore=self.getGroupScore(100,self.numcomponents,self.nummales,self.numunder18,self.numover70,self.avgage,self.minage,self.maxage)
        time = 1.2 * self.intensity  # 1.2 seconds per level of intensity, max intensity is 120 seconds per exercises
        exerciselist = []  # stretching/strenght
        time=self.adjustTimeGroupScore(time,groupscore)
        additionalbreaktime = self.getAdditionalBreakTime()
        if self.stretching:
            flexs = XmlManager(os.path.dirname(os.path.realpath(
                __file__)) + os.sep + "xmldata" + os.sep + "athlete_filters.xml").getFlexibilityexericises()
            exerciselist.append([(x, time, time / 2+additionalbreaktime) for x in flexs])  # list of (exercise, time, breaktime)
        if self.freeweight:
            strenghts = XmlManager(os.path.dirname(
                os.path.realpath(
                    __file__)) + os.sep + "xmldata" + os.sep + "athlete_filters.xml").getStrenghtexericisesKcalIntervalsGroup()
            exercises = [x[0] for x in strenghts]
            exerciseconsumptions = []
            for ex in exercises:
                exerciseconsumptions.append(self.getExerciseConsumptionGroupScore(exerciseskcals=strenghts, exercise=ex,groupscore=groupscore))
            averageconsumption = sum(exerciseconsumptions) / len(exerciseconsumptions)
            exerciseweights = []
            for ex in exerciseconsumptions:
                exweight = ex / averageconsumption
                if exweight > 1:
                    exweight = exweight - abs(1 - exweight) * 2
                elif exweight < 1:
                    exweight = exweight + abs(1 - exweight) * 2
                exerciseweights.append(exweight)
            tottime = self.kcal / averageconsumption  # in minutes
            times = []
            for exweight in exerciseweights:
                times.append(((tottime / len(exerciseweights)) * exweight) * 60)  # seconds
            repetitions = 1
            if 50<=self.intensity<75:
                for i in range(len(times)):
                    times[i]/=2
                repetitions=2
            elif 25<=self.intensity<50:
                for i in range(len(times)):
                    times[i]/=3
                repetitions=3
            elif self.intensity<25:
                for i in range(len(times)):
                    times[i]/=4
                repetitions=4
            for i in range(len(exercises)):
                #60 seconds break for intensity=100=maxvalue
                exerciselist.append((exercises[i],times[i],0.6*self.intensity+additionalbreaktime,repetitions))#list of (exercise, time, breaktime,repetitions)
        return exerciselist

    def getGroupScore(self, score, numcomponents, nummales, numunder18, numover70, avgage, minage, maxage):
        femaleratio=(numcomponents-nummales)/numcomponents
        under18ratio = numunder18 / numcomponents
        over70ratio = numover70 / numcomponents
        for ratio in [femaleratio,under18ratio,over70ratio]:
            if ratio > 0.85:
                score -= 5
            if ratio > 0.7:
                score -= 5
            if ratio > 0.55:
                score -= 5
            if ratio > 0.4:
                score -= 5
            if ratio > 0.25:
                score -= 5
            if ratio > 0.1:
                score -= 5
        if avgage>35:
            score-=5
        if avgage>50:
            score-=5
        if avgage>65:
            score-=5
        if avgage>75:
            score-=5
        if minage<13:
            score-=5
        if minage<10:
            score-=5
        if maxage>75:
            score-=5
        if maxage>80:
            score-=5

        return score
    def adjustTimeGroupScore(self, time, groupscore):
        if groupscore > 90:
            return time *1.2
        elif 80<groupscore <= 90:
            return time * 1.1
        elif 60<=groupscore < 70 and groupscore:
            return time *0.8
        elif groupscore < 60:
            return time * 0.9
        return time

    def getAdditionalBreakTime(self):
        additionalbreaktime=0
        if self.numcomponents >= 15:
            additionalbreaktime += 5
            if self.numcomponents >= 30:
                additionalbreaktime += 5
        return additionalbreaktime

    def getExerciseConsumptionGroupScore(self, exerciseskcals, exercise,groupscore):
        for i in range(len(exerciseskcals)):
            if exerciseskcals[i][0]==exercise:
                for j in range(len(exerciseskcals[i][1])):
                    if exerciseskcals[i][1][j][1]<=groupscore<exerciseskcals[i][1][j][0]:
                        return exerciseskcals[i][1][j][2]