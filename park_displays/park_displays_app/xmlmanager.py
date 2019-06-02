import xml.etree.ElementTree as ET

class XmlManager():
    def __init__(self, filepath):
        filepath=filepath
        tree = ET.parse(filepath)
        self.root = tree.getroot()

    def getFountains(self):
        enggart = self.root.find('englischer_garten')
        fountains = enggart.findall('fountains')
        fountainlist = []
        for fountain in fountains:
            for node in fountain.getiterator():
                try:
                    fountainlist.append((node.attrib["lat"], node.attrib["lng"]))
                except:
                    pass
    def getPaths(self):
        pathlist = []
        for child in self.root.iter('englischer_garten'):
            print(child.tag, child.attrib)
            for childt in child:
                if childt.tag == 'paths':
                    for childu in childt:
                        if childu.tag == 'path':
                            path = [None, None, None, []]
                            terrain = childu.attrib["terrain"]
                            path[0] = terrain
                            for childr in childu:
                                if childr.tag == "start":
                                    start = (childr.attrib["lat"], childr.attrib["lng"])
                                    path[1] = start
                                if childr.tag == "waypoints":
                                    for childf in childr:
                                        waypoint = (childf.attrib["lat"], childf.attrib["lng"])
                                        path[3].append(waypoint)

                                if childr.tag == "end":
                                    end = (childr.attrib["lat"], childr.attrib["lng"])
                                    path[2] = start
                            pathlist.append(path)
        return pathlist