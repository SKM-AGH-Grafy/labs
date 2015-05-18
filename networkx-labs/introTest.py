
__author__ = 'kuban'

import networkx as nx
import matplotlib.pyplot as plt


K_3_5=nx.complete_bipartite_graph(3,5)
nx.draw(K_3_5)
plt.savefig("K35")