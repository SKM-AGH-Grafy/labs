__author__ = 'kuban'

from twitter.OAuth import api
import networkx as nx
import matplotlib.pyplot as plt

class twitterGraphGenerator():

    def __init__(self,userStartName):
        self.graph = nx.Graph()
        self.startUser = api.get_user(userStartName)
        self.startUserID = self.startUser.id
        self.colors = {}
        self.distances = {}
        self.parents = {}
        self.container = []
        for vertex in nx.nodes(self.graph):
            self.colors[vertex]="White"
    def addVertexToContainer(self, vertex):
        self.container.append(vertex)
        self.colors[vertex]="Blue"
        self.addVertexToGraph(vertex)
    def addVertexToGraph(self,vertexID):
        if vertexID not in self.graph.node.keys():
            self.graph.add_node(vertexID,name = "Not Set")
    def addVertexToGraphWithCorrectName(self,vertexID):
        if vertexID not in self.graph.node.keys():
            user = api.get_user(vertexID)
            self.graph.add_node(user.id,name = user.name)
    def getVertexFromContainer(self):
        return self.container.pop(0)
    def isContainerEmpty(self):
        return len(self.container)==0
    def getNeighboursForVertex(self,vertexID, max_offset=-1):
        neighbours_lists = api.followers_ids(vertexID)
        if max_offset == -1:
            max = len(neighbours_lists)
        else :
            max = max_offset
        return neighbours_lists[:max]
    def addEdgeToGraph(self,startVertexID,endVertexID):
        self.graph.add_edge(startVertexID,endVertexID)
    def isVertexVisited(self,vertex):
        return vertex in self.graph.node
    def generateFollowersNetwork(self,maxOffset,depth):
        self.addVertexToContainer(self.startUserID)
        self.parents[self.startUserID]=None
        self.distances[self.startUserID]=0
        self.addVertexToGraph(self.startUserID)
        while not self.isContainerEmpty():
            v = self.getVertexFromContainer()
            if (self.distances[v]>depth):
                continue
            for neighbour in self.getNeighboursForVertex(v,maxOffset):
                if self.isVertexVisited(neighbour):
                    pass
                else :
                    self.addVertexToContainer(neighbour)
                    self.addVertexToGraph(neighbour)
                    self.addEdgeToGraph(v,neighbour)
                    self.distances[neighbour]=self.distances[v]+1
                    self.parents[neighbour]=v
    def getShortestPath(self,startVertex,endVertex):
        result = [endVertex]
        vertex = endVertex
        while vertex != startVertex:
            vertex = self.parents[vertex]
            result.append(vertex)
        return result[::-1]
    def getShortestPathWithNames(self,startVertex,endVertex):
        pathWithID = self.getShortestPath(startVertex,endVertex)
        result=[]
        for id in pathWithID:
            result.append(self.getNameForID(id))
        return result

    def getIDForName(self,name):
        user = api.get_user(name)
        return user.id
    def getNameForID(selfself,id):
        user = api.get_user(id)
        return user.name
    def getShortestPathWithNamesBetweenUserNames(self,startUserName,endUserName):
        return self.getShortestPathWithNames(self.getIDForName(startUserName),self.getIDForName(endUserName))





