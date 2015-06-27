__author__ = 'kuban'


from random import __all__
import networkx as nx
import matplotlib.pyplot as plt
from mrowki.mrowka import Mrowka

class Algorytm:
    def __init__(self, G, l_mrowek, pvalue, wierzcholekPoczatkowy, q0, alfa, beta, tau0):
        self.G = G
        self.potrzebnaIloscKrokow = len(self.G.nodes)-1
        self.l_mrowek = l_mrowek
        self.q0=q0
        self.alfa = alfa
        self.beta = beta
        self.tau0 = tau0
        self.listaMrowek=[]
        self.wierzcholekPoczatkowy = wierzcholekPoczatkowy
        self.pvalue = pvalue
        self.stworzMrowki()

    def stworzMrowke(self, name):
        mrowka = Mrowka(name,self.pvalue, self.wierzcholekPoczatkowy, self.alfa, self.tau0,self.beta)
        self.listaMrowek.append(mrowka)
    def stworzMrowki(self):
        for i in range(self.l_mrowek):
            self.stworzMrowke("Mrowka "+str(i))

    def wykonajKrokMrowek(self):
        for mrowka in self.listaMrowek:
            mrowka.wykonajKrok(self.G)

    def stworzMrowkiOdNowa(self):
        self.listaMrowek=[]
        self.stworzMrowki()

    def wykonajIteracje(self):
        self.stworzMrowki()
        for i in range(self.potrzebnaIloscKrokow):
            self.wykonajKrokMrowek()
        najlepszaMrowkaIDlugoscCyklu = self.zwrocNajlepszaMrowkeIdlugoscCyklu()
        self.nagrodzMrowke(najlepszaMrowkaIDlugoscCyklu)

    def zwrocNajlepszaMrowkeIdlugoscCyklu(self):
        mrowkiZDlugosciamiCyklow = {mrowka: mrowka.wyliczDlugoscCyklu(self.G) for mrowka in self.listaMrowek}
        maxValue = max(mrowkiZDlugosciamiCyklow.values())
        for key, value in mrowkiZDlugosciamiCyklow.values():
            if value == maxValue:
                maxArg = key
        return maxArg,maxValue

    def nagrodzMrowke(self,mrowkaIDlugoscCyklu):
        mrowka=mrowkaIDlugoscCyklu[0]
        dlCyklu = mrowkaIDlugoscCyklu[1]
        for i in range(-1,(len(mrowka.sciezka)-1)):
            wierzchStart = mrowka.sciezka[i]
            wierzchKonc = mrowka.sciezka[i+1]
            nowaWartoscFeromonu = self.wyliczNowaWartoscFeromonu(wierzchStart,wierzchKonc,mrowka,dlCyklu)
            self.G.zmodyfikujWartoscF(wierzchStart,wierzchKonc,nowaWartoscFeromonu)

    def zwrocNajkrotszyCykl(self):
        pass

    def wyliczNowaWartoscFeromonu(self, wierzchStart,wierzchKonc,mrowka,dlCyklu):
        nowaWartosc = (1-self.alfa)*self.G.pobierzWartoscF(wierzchStart,wierzchKonc)+self.alfa*dlCyklu
        return nowaWartosc

    def wykonajAlgorytm(self,iloscIteracji):
        for runda in range(iloscIteracji):
            self.wykonajIteracje()



G=nx.read_gpickle("resources/cities.gpickle")

print("Koniec")