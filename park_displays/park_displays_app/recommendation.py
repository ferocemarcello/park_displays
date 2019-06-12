import os

from .data_manager import ParkManager
from .xmlmanager import XmlManager
from pprint import pprint
import requests
class RunWalkRecommender():
    def __init__(self,path_types,gender,age,weight,height,kcal,avgweekkm,shoetype,activity):
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
        #weather = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Munich&APPID=676536c0f3533a7868a16beed9f14ba4')
        prweather=(weather.json())
        if self.activity=='running':
            return self.recommendRunning()
        else:
            return self.recommendWalking()
    def recommendRunning(self):
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