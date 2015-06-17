__author__ = 'kuban'

import random
import networkx as nx
import matplotlib.pyplot as plt

class Mrowka:
   def __init__(self, imie, pvalue):
       sciezka = []
       self.imie = imie
       self.pvalue = pvalue

   def dodajWierzcholekDoSciezki(self, graf):
       losowa = random.random()
       if losowa<self.pvalue:
           graf.adjacency_list()


