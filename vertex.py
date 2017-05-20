from path import Path
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.direction = {}

    def addNeighbor(self,nbr,di,weight=0):
        self.connectedTo[nbr] = weight
        self.direction[nbr] = di

    def addNeighbors(self, nbr):
        self.connectedTo[nbr.getId()] = nbr

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()


    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def getDirection(self, nbr):
        return self.direction[nbr]
