__author__ = 'kuban'

from rozwiazania.lab2.Vertex import Vertex
from rozwiazania.lab2.graph import Graph

class ShortestPathFinder():
    def __init__(self, graph):
        self.graph = graph
        self.colors = {}
        self.distances = {}
        self.parents = {}
        self.container = []
        for vertex in graph.vertices:
            self.colors[vertex]="White"
    def addVertexToContainer(self, vertex):
        self.container.append(vertex)
        self.colors[vertex]="Blue"
    def getVertexFromContainer(self):
        return self.container.pop(0)
    def isContainerEmpty(self):
        return len(self.container)==0
    def isVertexVisited(self,vertex):
        return self.colors[vertex]=="Blue"
    def getPathBetweenVertices(self,startVertex,endVertex):
        self.addVertexToContainer(startVertex)
        self.parents[startVertex]=None
        self.distances[startVertex]=0
        while not self.isContainerEmpty():
            v = self.getVertexFromContainer()
            for neighbour in v.neighbours:
                if self.isVertexVisited(neighbour):
                    pass
                else :
                    self.addVertexToContainer(neighbour)
                    self.distances[neighbour]=self.distances[v]+1
                    self.parents[neighbour]=v
        result=[endVertex]
        vertex = endVertex
        while vertex != startVertex:
            vertex = self.parents[vertex]
            result.append(vertex)
        return result[::-1]
    def printPath(self,lista):
        result=""
        for vertex in lista:
            result = result + vertex.name+"-->"
        return result[:-3]



v0 =Vertex(0)
v1 = Vertex(1)
v2 = Vertex(2)
v3 = Vertex(3)
v4 = Vertex(4)
v5 = Vertex(5)
v6 = Vertex(6)
v7 = Vertex(7)
v8 = Vertex(8)
g=Graph("G")
g.addEdge(v0,v1)
g.addEdge(v0,v3)
g.addEdge(v0,v4)
g.addEdge(v4,v5)
g.addEdge(v4,v7)
g.addEdge(v7,v6)
g.addEdge(v7,v3)
g.addEdge(v5,v1)
g.addEdge(v5,v6)
g.addEdge(v6,v8)
g.addEdge(v2,v1)
g.addEdge(v2,v3)
g.addEdge(v2,v6)
# print(g)

a = ShortestPathFinder(g)
result = a.getPathBetweenVertices(v0,v8)
print(a.printPath(result))