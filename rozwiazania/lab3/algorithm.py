from rozwiazania.lab2.Vertex import Vertex
from rozwiazania.lab2.graph import Graph

__author__ = 'kuban'


class ShortestPathFinder(object):
    def __init__(self, graph):
        self.graph = graph
        self.container = []
        self.visitedVertices = set()
        self.poprzednicy = dict()
    def addVertexToContainer(self, vertex):
        self.container.append(vertex)
    def getNextVertexFromContainer(self):
        return self.container.pop(0)
    def isVertexVisited(self, vertex):
        return vertex in self.visitedVertices
    def markVertexAsVisited(self, vertex):
        self.visitedVertices.add(vertex)
    def findPathBetweenVertices(self, startVertex, endVertex):
        self.addVertexToContainer(startVertex)
        self.markVertexAsVisited(startVertex)
        self.poprzednicy[startVertex] = None
        v = startVertex
        while len(self.container)!=0:
            v = self.getNextVertexFromContainer()
            if v == endVertex:
                break
            for neighbour in v.neighbours:
                if self.isVertexVisited(neighbour):
                    pass
                else :
                    self.poprzednicy[neighbour] = v
                    self.addVertexToContainer(neighbour)
                    self.markVertexAsVisited(neighbour)
        result=[]
        while v is not None:
            result.append(v)
            v=self.poprzednicy[v]
        return result[::-1]
    def printPath(self,path):
        res = ""
        for elem in path:
            res = res + elem.name+"-->"
        return res[:-3]

v1 = Vertex(1)
v2 = Vertex(2)
v3 = Vertex(3)
v4 = Vertex(4)
v5 = Vertex(5)
v6 = Vertex(6)
g=Graph("G")
g.addEdge(v1,v2)
g.addEdge(v1,v3)
g.addEdge(v1,v4)
g.addEdge(v2,v3)
g.addEdge(v3,v4)
g.addEdge(v2,v5)
g.addEdge(v5,v6)
print(g)

algorithm = ShortestPathFinder(g)
path = algorithm.findPathBetweenVertices(v1,v6)
print(algorithm.printPath(path))

