__author__ = 'kuban'

import random
import networkx as nx
import matplotlib.pyplot as plt
import math

class Mrowka:
    def __init__(self, imie, pvalue, wierzcholekPoczatkowy):
        self.sciezka = [wierzcholekPoczatkowy]
        self.imie = imie
        self.pvalue = pvalue

   def pobierzFeromonySasiadow(self, graf):
       nieodwiedzone = [x for x in graf.adjacency_list() if x not in self.sciezka]
       slownik = {x: graf.pobierzWartoscF(self.pobierzAktualnyWierzcholek(), x) for x in nieodwiedzone}
       return slownik

   def dodajWierzcholekDoSciezki(self, graf):
       losowa = random.random()
       if losowa<self.pvalue:
           slownik = self.pobierzFeromonySasiadow(graf)
           maxValue = max(slownik.values())
           for key, value in slownik.values():
               if value == maxValue:
                   maxArg = key
       self.sciezka.append(maxArg)
       else:
           pass
   #TODO: Znaleźć sensowny sposób na zdefiniowanie zmiennej losowej na podstawie funkcji



   def pobierzAktualnyWierzcholek(self):
       return self.sciezka[-1]

   def wykonajKrok(self, graf):
       self.dodajWierzcholekDoSciezki(graf)


G=nx.Graph()
l=G.adjacency_list()


