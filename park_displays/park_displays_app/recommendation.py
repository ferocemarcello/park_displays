class RunWalkRecommender():
    def __init__(self,gender,age,weight,height,kcal,avgweekkm,activity):
        self.gender=gender
        self.age=age
        self.weight=weight
        self.height=height
        self.kcal=kcal
        self.avgweekkm=avgweekkm
        self.activity=activity
    def recommendPaths(self):
        return [(None,None,None,None)]#pathid,#warmup,#cooldown,#avgspeed
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