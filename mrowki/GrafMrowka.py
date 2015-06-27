__author__ = 'kuban'


from random import __all__
import networkx as nx
import matplotlib.pyplot as plt

class GrafMrowka(nx.Graph):
    def __init__(self,graph,tau0):
        super().__init__(graph)
        self.tau0 = tau0
        self.ustalPoczatkowyFeromon()
    def ustalPoczatkowyFeromon(self):
        for edge in self.edges():
            edge.feromon=self.tau0
    def pobierzWartoscF(self, wS,wK):
        return self.edge[wS][wK].feromon
    def zmodyfikujWartoscF(self,wS,wK,nowaWartosc):
        self.edge[wS][wK].feromon = nowaWartosc
    def pobierzOdleglosc(self,MiastoStart, MiastoKonc):
        return self.edge[MiastoStart][MiastoKonc]['weight']

g=nx.Graph()
G=GrafMrowka(g)
G.adjacency_list()