__author__ = 'kuban'


from random import __all__
import networkx as nx
import matplotlib.pyplot as plt
from mrowka import Mrowka

class Algorytm:
    def __init__(self, G, l_mrowek, q0, alfa, beta, tau0):
        self.G = G
        self.l_mrowek = l_mrowek
        self.q0=q0
        self.alfa = alfa
        self.beta = beta
        self.tau0 = tau0
        self.listaMrowek=[]
    def stworzMrowke(self, name):
        mrowka = Mrowka(name,self.q0)
        self.listaMrowek.append(mrowka)
    def wykonajKrokMrowek(self):
        for mrowka in self.listaMrowek:
            mrowka.wykonajKrok(self.G)
    def wykonajIteracje(self):
        pass
    def porownajMrowki(self):
        pass
    def nagrodzMrowke(self):
        pass
    def zwrocNajkrotszyCykl(self):
        pass

G=nx.read_gpickle("resources/cities.gpickle")

print("Koniec")