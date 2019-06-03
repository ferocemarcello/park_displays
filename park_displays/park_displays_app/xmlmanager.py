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
    def getPaths(self,parkname):
        pathlist = []
        for child in self.root.iter('park'):
            if child.attrib["name"]==parkname:
                for parkchild in child:
                    if parkchild.tag == 'paths':
                        for pathschild in parkchild:
                            if pathschild.tag == 'path':
                                path = [None, None, None, []]
                                terrain = pathschild.attrib["terrain"]
                                path[0] = terrain
                                for pathelement in pathschild:
                                    if pathelement.tag == "start":
                                        start = (pathelement.attrib["lat"], pathelement.attrib["lng"])
                                        path[1] = start
                                    if pathelement.tag == "waypoints":
                                        for childf in pathelement:
                                            waypoint = (childf.attrib["lat"], childf.attrib["lng"])
                                            path[3].append(waypoint)

                                    if pathelement.tag == "end":
                                        end = (pathelement.attrib["lat"], pathelement.attrib["lng"])
                                        path[2] = end
                                pathlist.append(path)
        return pathlist