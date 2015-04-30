__author__ = 'kuban'


class Vertex(object):
    def __init__(self,name,weight=0):
        self.name = name
        self.weight = weight
    def __lt__(self, other):
        return self.weight < other.weight
    def __str__(self):
        return "Wierzchołek : " + self.name





v1=Vertex("Pierwszy",2)
v2=Vertex("Drugi",1)
v3=Vertex("Trzeci",4)

L=[v1,v2,v3]
liczby=[1,2,3,8,5]
liczby.sort()
print(liczby)
A=L.sort()
#print(v1)
for i in L:
    print(i)
