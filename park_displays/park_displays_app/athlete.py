from .user import User

class Athlete(User):
    '''usage:
    athlete=Athlete(name="Fred",surname="Bob",email="dfafa", gender="Male", sport="Running", height=184, weight=74, age=23)
    user=User(name="Fred",surname="Bob",email="dfafa", gender="Male")
    ath2=Athlete(user=user,sport="Running", height=184, weight=74,age=23)'''
    def __init__(self, sport,height, weight, age,name=None,surname=None, gender=None,email=None, user:User=None):
        if not user:
            self.sport = sport
            self.height = height
            self.weight = weight
            self.age = age
            super().__init__(name=name, surname=surname, gender=gender, email=email)
        else:
            self.sport = sport
            self.height = height
            self.weight = weight
            self.age = age
            super().__init__(name=user.name, surname=user.surname, gender=user.gender, email=user.email)