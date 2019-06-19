import xml.etree.ElementTree as ET

class XmlManager():
    def __init__(self, filepath):
        filepath=filepath
        tree = ET.parse(filepath)
        self.root = tree.getroot()

    def getFountains(self,parkname):
        for child in self.root.iter('park'):
            if child.attrib["name"]==parkname:

                fountainlist = []
                for c in child:
                    if c.tag == 'fountains':
                        for f in c:
                            if f.tag=="fountain":
                                fountainlist.append((f.attrib["lat"],f.attrib["lng"]))
                return fountainlist
    def getGroups(self,parkname):
        for child in self.root.iter('park'):
            if child.attrib["name"]==parkname:

                grouplist = []
                for c in child:
                    if c.tag == 'groups':
                        for f in c:
                            if f.tag=="group":
                                grouplist.append(((f.attrib["lat"],f.attrib["lng"]),f.attrib["stretching"]=="True",f.attrib["freeweight"]=="True"))
                return grouplist
    def getMinMaxNumGroupFilter(self,groupFilter):
        for child in self.root.iter('filters'):
            for filter in child:
                if filter.tag == groupFilter:
                    return (filter.attrib["min"], filter.attrib["max"])
    def getGymTools(self,parkname):
        for child in self.root.iter('park'):
            if child.attrib["name"]==parkname:
                toollist = []
                for c in child:
                    if c.tag == 'gymtools':
                        for f in c:
                            if f.tag=="gymtool":
                                toollist.append((f.text,(f.attrib["lat"],f.attrib["lng"])))
                return toollist
    def getGymToolsScore(self):
        for child in self.root.iter('gymtooltypes'):
                toollist = []
                for c in child:
                    if c.tag == 'gymtooltype':
                        toollist.append((c.text,{"frontabs":c.attrib["frontabs"],"sideabs":c.attrib["sideabs"],"arms":c.attrib["arms"],"highlegs":c.attrib["highlegs"],"lowlegs":c.attrib["lowlegs"],"chest":c.attrib["chest"],"back":c.attrib["back"]}))
                return toollist
    def getAthletes(self):
        athletes = []
        for child in self.root.iter('athletes'):
            for c in child:
                if c.tag=="athlete":
                    athletes.append((c.attrib["id"],c.attrib["age"],c.attrib["height"],c.attrib["weight"],c.attrib["shoetype"]))
        return athletes
    def getAthlete(self,athleteid):
        for child in self.root.iter('athletes'):
            for c in child:
                if c.tag=="athlete" and c.attrib["id"]==str(athleteid):
                    return (c.attrib["id"],c.attrib["age"],c.attrib["height"],c.attrib["weight"],c.attrib["shoetype"])
    def getGenders(self):
        genders=[]
        for child in self.root.iter('genders'):
            for gender in child:
                genders.append(gender.text)
        return genders
    def getShoeTypes(self):
        shoetypes=[]
        for child in self.root.iter('shoetypes'):
            for gender in child:
                shoetypes.append(gender.text)
        return shoetypes
    def getPathTypes(self):
        pathtypes=[]
        for child in self.root.iter('pathtypes'):
            for pathtype in child:
                pathtypes.append(pathtype.text)
        return pathtypes
    def getToolTypes(self):
        gymtooltypes = []
        for child in self.root.iter('gymtooltypes'):
            for gymtooltype in child:
                gymtooltypes.append(gymtooltype.text)
        return gymtooltypes
    def getBodyParts(self):
        bodyparts = []
        for child in self.root.iter('bodyparts'):
            for bodypart in child:
                bodyparts.append(bodypart.text)
        return bodyparts
    def getStrenghtexericises(self):
        strenghtexericises = []
        for child in self.root.iter('strenghtexericises'):
            for strenghtexericise in child:
                strenghtexericises.append(strenghtexericise.text)
        return strenghtexericises
    def getFlexibilityexericises(self):
        flexibilityexercises = []
        for child in self.root.iter('flexibilityexercises'):
            for flexibilityexercise in child:
                flexibilityexercises.append(flexibilityexercise.text)
        return flexibilityexercises
    def getAgeIntervals(self):
        ageintervals=[]
        for child in self.root.iter('ageintervals'):
            for ageinterval in child:
                ageintervals.append(ageinterval.text)
        return ageintervals
    def getKcalIntervals(self):
        kcalintervals=[]
        for child in self.root.iter('kcalintervals'):
            for kcalinterval in child:
                kcalintervals.append(kcalinterval.text)
        return kcalintervals
    def getWeightIntervals(self):
        weightintervals=[]
        for child in self.root.iter('weightintervals'):
            for weightinterval in child:
                weightintervals.append(weightinterval.text)
        return weightintervals
    def getHeightIntervals(self):
        heightintervals=[]
        for child in self.root.iter('heightintervals'):
            for heightinterval in child:
                heightintervals.append(heightinterval.text)
        return heightintervals
    def getTrainingTypes(self):
        types = []
        for child in self.root.iter('trainingtypes'):
            for type in child:
                types.append(type.text)
        return types
    def getPaths(self,parkname):
        pathlist = []
        for child in self.root.iter('park'):
            if child.attrib["name"]==parkname:
                for parkchild in child:
                    if parkchild.tag == 'paths':
                        for pathschild in parkchild:
                            if pathschild.tag == 'path':
                                path = [None,[]]
                                terrain = pathschild.attrib["terrain"]
                                height_d = pathschild.attrib["height_difference"]
                                steepness= pathschild.attrib["steepness"]
                                length = pathschild.attrib["length"]
                                path[0] = (terrain,height_d,steepness,length)
                                for pathelement in pathschild:
                                    if pathelement.tag == "waypoints":
                                        for childf in pathelement:
                                            waypoint = (childf.attrib["lat"], childf.attrib["lng"])
                                            path[1].append(waypoint)
                                pathlist.append(path)
        return pathlist

    def getRunners(self, parkname):
        for child in self.root.iter('park'):
            if child.attrib["name"]==parkname:

                runnerlist = []
                for c in child:
                    if c.tag == 'running':
                        for f in c:
                            if f.tag=="athlete":
                                runnerlist.append((f.attrib["lat"],f.attrib["lng"]))
                return runnerlist

    def getWalkers(self, parkname):
        for child in self.root.iter('park'):
            if child.attrib["name"]==parkname:

                walkerlist = []
                for c in child:
                    if c.tag == 'walking':
                        for f in c:
                            if f.tag=="athlete":
                                walkerlist.append((f.attrib["lat"],f.attrib["lng"]))
                return walkerlist

    def getGymAthletes(self, parkname):
        for child in self.root.iter('park'):
            if child.attrib["name"]==parkname:

                gymathletelist = []
                for c in child:
                    if c.tag == 'outdoorgym':
                        for f in c:
                            if f.tag=="athlete":
                                gymathletelist.append((f.attrib["lat"],f.attrib["lng"]))
                return gymathletelist

    def getFreeweightAthletes(self, parkname):
        for child in self.root.iter('park'):
            if child.attrib["name"]==parkname:

                freeweightlist = []
                for c in child:
                    if c.tag == 'freeweight':
                        for f in c:
                            if f.tag=="athlete":
                                freeweightlist.append((f.attrib["lat"],f.attrib["lng"]))
                return freeweightlist

    def getStretchers(self, parkname):
        for child in self.root.iter('park'):
            if child.attrib["name"]==parkname:

                stretcherlist = []
                for c in child:
                    if c.tag == 'stretching':
                        for f in c:
                            if f.tag=="athlete":
                                stretcherlist.append((f.attrib["lat"],f.attrib["lng"]))
                return stretcherlist
