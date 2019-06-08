from .xmlmanager import XmlManager


class ParkManager:
    def __init__(self, parkname,xmlmanager: XmlManager):
        self.parkname=parkname
        self.xmlmanager=xmlmanager
    def getPaths(self):
        return self.xmlmanager.getPaths(self.parkname)
    def getPathsWaypoints(self):
        pathswaypoints=[]
        paths = self.getPaths()
        for path in paths:
            pathswaypoints.append(path[1])
        return pathswaypoints
    def getPathTypes(self):
        pathtypes = [[], [], []]
        paths=self.getPaths()
        for path in paths:
            terraintype = path[0][0]
            if terraintype == "pavement":
                pathtypes[0].append(paths.index(path))
            if terraintype == "gravel":
                pathtypes[1].append(paths.index(path))
            if terraintype == "dirt":
                pathtypes[2].append(paths.index(path))
        return pathtypes
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
class DataProcesser:
    def __init__(self):
        pass
    @staticmethod
    def listIntoDict(lis):
        dic=dict()
        for i in range(len(lis)):
            dic[i]=lis[i]
        return dic