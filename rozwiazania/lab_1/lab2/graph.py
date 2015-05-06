from rozwiazania.lab_1.lab2.Vertex import Vertex

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


v1 = Vertex(1)
v2 = Vertex(2)
v3 = Vertex(3)
v4 = Vertex(4)
v5 = Vertex(5)
g=Graph("G")
g.addEdge(v1,v2)
g.addEdge(v1,v3)
g.addEdge(v1,v4)
g.addEdge(v2,v3)
g.addEdge(v3,v4)
g.addEdge(v2,v5)
print(g)



