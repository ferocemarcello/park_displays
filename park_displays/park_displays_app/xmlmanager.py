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