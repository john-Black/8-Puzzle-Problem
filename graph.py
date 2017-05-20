from vertex import Vertex
from path import Path
from breadthFirst import BreadthFirst
import random

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.expl = []
        self.bFs = BreadthFirst()


#add vertexes to the graph
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        self.bFs.addNode(key, newVertex)
        return newVertex
#get vertexes of the graph
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,di,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], di, cost)
        self.vertList[t].addNeighbor(self.vertList[f], self.getPlace(di), cost)
    def getPlace(self, di):
        if di == "UP":
            return "DOWN"

        elif di == "DOWN":
            return "UP"
            
        elif di == "LEFT":
            return "RIGHT"
            
        elif di == "RIGHT":
            return "LEFT"

        else:
            return "Unknown"


    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())



    def bfs(self, start, goal):
        a, b = self.bFs.run(start, goal)
        return b


#gets the neighbors of the node
    def getNeighbors(self, key):
        n = []
        for a in list(self.vertList[key].getConnections()):
            n.append(a.getId())

        return n

    def getTree(self, gr):
        for a in gr:
            print(a, self.getNeighbors(a))






    def printGraph(self):
        for f, v in self.vertList.items():
            for w in v.getConnections():
                print("( %s , %s )" % (v.getId(), w.getId()))



    def setMatrix(self, di):
        for a in range(len(di)):
            for b in range(len(di[a])):
                if b + 1 != len(di[a]):
                    self.addEdge(di[a][b], di[a][b + 1], "RIGHT", random.randrange(1, 9))
                if a != 0:
                    self.addEdge(di[a][b], di[a - 1][b], "UP", random.randrange(1, 9))


