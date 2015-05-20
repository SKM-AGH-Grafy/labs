import pickle
from twitter.graphGenerator import twitterGraphGenerator


__author__ = 'kuban'


tGraph = twitterGraphGenerator("qbahn")
tGraph.generateFollowersNetwork(5,3)

graphName ="qbahn-5-3"

with open("graphs/twitterNetwork-"+graphName+".txt",'wb') as file:
    pickle.dump(tGraph, file)



