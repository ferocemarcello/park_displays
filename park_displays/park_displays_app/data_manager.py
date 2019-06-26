from .xmlmanager import XmlManager
from math import sin, cos, sqrt, atan2, radians


def getDistanceCoordinates(parklocation, location):
    # approximate radius of earth in metres
    R = 6373000.0

    lat1 = radians(parklocation[0])
    lon1 = radians(parklocation[1])
    lat2 = radians(location[0])
    lon2 = radians(location[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c


class ParkManager:
    def __init__(self, parkname,xmlmanager: XmlManager,pathtypes=[],gymtooltypes=[]):
        self.parkname=parkname
        self.xmlmanager=xmlmanager
        self.pathtypes=pathtypes
        self.gymtooltypes=gymtooltypes
    def getPaths(self):
        return self.xmlmanager.getPaths(self.parkname)
    def getPathsWaypoints(self):
        pathswaypoints=[]
        paths = self.getPaths()
        for path in paths:
            pathswaypoints.append(path[1])
        return pathswaypoints
    def getPathsByType(self):
        paths = self.getPaths()
        pathsbytype=[]
        for i in range(len(self.pathtypes)):
            pathsbytype.append([])
        for path in paths:
            terraintype = path[0][0]
            pathsbytype[self.pathtypes.index(terraintype)].append(paths.index(path))
        return pathsbytype
    def getGymToolsByType(self):
        gymtools = self.getGymTools()
        gymtooltypes=[]
        for i in range(len(self.gymtooltypes)):
            gymtooltypes.append([])
        for gymtool in gymtools:
            gymtooltype = gymtool[0]
            gymtooltypes[self.gymtooltypes.index(gymtooltype)].append(gymtools.index(gymtool))
        return gymtooltypes
    def getPathsSlopes(self):
        paths = self.getPaths()
        pathslopes=[]
        for path in paths:
            pathslopes.append(path[0][2])
        return pathslopes
    def getPathsHeightdiffs(self):
        paths = self.getPaths()
        pathsheightdiffs = []
        for path in paths:
            pathsheightdiffs.append(path[0][1])
        return pathsheightdiffs
    def getPathsLengths(self):
        paths = self.getPaths()
        pathslengths = []
        for path in paths:
            pathslengths.append(path[0][3])
        return pathslengths
    def getFountains(self):
        return self.xmlmanager.getFountains(parkname=self.parkname)
    def getGymTools(self):
        return self.xmlmanager.getGymTools(parkname=self.parkname)
    def getRunners(self):
        return self.xmlmanager.getRunners(parkname=self.parkname)
    def getWalkers(self):
        return self.xmlmanager.getWalkers(parkname=self.parkname)
    def getGymAthletes(self):
        return self.xmlmanager.getGymAthletes(parkname=self.parkname)
    def getFreeweightAthletes(self):
        return self.xmlmanager.getFreeweightAthletes(parkname=self.parkname)
    def getStretchers(self):
        return self.xmlmanager.getStretchers(parkname=self.parkname)
    def getGroups(self):
        return self.xmlmanager.getGroups(parkname=self.parkname)

    @classmethod
    def getParkFromLocation(cls, location, xmlmanager:XmlManager):
        parklist=xmlmanager.getParkList()
        for park in parklist:
            if getDistanceCoordinates(park[1],location)<1000:
                return park
        return parklist[0]


class AthleteManager:
    def __init__(self, athleteid,xmlmanager: XmlManager):
        self.athleteid=athleteid
        self.xmlmanager=xmlmanager
    def getShoeType(self):
        return self.xmlmanager.getAthlete(self.athleteid)[4]
class DataProcesser:
    def __init__(self):
        pass
    @staticmethod
    def listIntoDict(lis):
        dic=dict()
        for i in range(len(lis)):
            dic[i]=lis[i]
        return dic