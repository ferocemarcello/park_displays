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