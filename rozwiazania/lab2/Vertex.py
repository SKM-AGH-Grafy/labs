__author__ = 'kuban'


class Vertex():
    def __init__(self,name):
        self.name = str(name)
        self.neighbours =[]
    def __eq__(self, other):
        return self.name == other.name
    def addNeighbour(self, neighbour):
        self.neighbours.append(neighbour)
    def isNeighbour(self,vertex):
        return vertex in self.neighbours
    def __str__(self):
        result=self.name+"-->"
        for neighbour in self.neighbours:
            result=result+neighbour.name+","
        return result[:-1]
    def __hash__(self):
        return self.name.__hash__()




b=Vertex("v")
a=Vertex("v")
print(a)
# #a.addNeighbour(b)
# print(a.isNeighbour(b))
# c=object()
# print(c.__eq__(c))
print(a==b)
print(Vertex.isNeighbour)