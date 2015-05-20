__author__ = 'kuban'


import pickle
from twitter.graphGenerator import twitterGraphGenerator
import networkx as nx
import matplotlib.pyplot as plt


graphName ="qbahn-5-2"
tGraph = None
with open("graphs/twitterNetwork-"+graphName+".txt",'rb') as file:
    tGraph = pickle.load(file)

nx.draw(tGraph.graph)
plt.savefig("graphs/"+graphName)

