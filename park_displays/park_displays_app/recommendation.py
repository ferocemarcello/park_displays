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
        return []
class GymRecommender():
    def __init__(self,gender,age,weight,height,kcal,bodyparts:[]):
        self.gender=gender
        self.age=age
        self.weight=weight
        self.height=height
        self.kcal=kcal
        self.bodyparts=bodyparts
    def recommendPaths(self):
        return [(None,None,None)]#list of (machine, time, intensity)   intensity can be speed, weight, Force...