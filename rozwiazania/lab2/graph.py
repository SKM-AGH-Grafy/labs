from rozwiazania.lab2.Vertex import Vertex

__author__ = 'kuban'


class Graph(object):

    def __init__(self,name):
        self.name = name
        self.vertices=set()
    def addVertex(self,newVertex):
        self.vertices.add(newVertex)
    def addEdge(self,v1,v2):
        v1.addNeighbour(v2)
        v2.addNeighbour(v1)
        self.addVertex(v1)
        self.addVertex(v2)
    def __str__(self):
        result = "Graf "+self.name+ ": \n \n"
        for vertex in self.vertices:
            result = result + str(vertex)+"\n"
        return result


g=Graph("G")
v1 = Vertex("1")
g.addVertex(v1)



