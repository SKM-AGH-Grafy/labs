__author__ = 'kuban'

import random
import networkx as nx
import matplotlib.pyplot as plt
import math
import scipy.stats as st

class Mrowka(object):
    def __init__(self, imie, pvalue, wierzcholekPoczatkowy, alfa, tau0, beta):
        self.sciezka = [wierzcholekPoczatkowy]
        self.imie = imie
        self.pvalue = pvalue
        self.alfa = alfa
        self.tau0 = tau0
        self.beta = beta

    def pobierzListeNieodwiedzonychWierzcholkow(self, graf):
        nieodwiedzone = [x for x in graf.adjacency_list() if x not in self.sciezka]
        return nieodwiedzone

    def pobierzFeromonySasiadow(self, graf):
        nieodwiedzone = self.pobierzListeNieodwiedzonychWierzcholkow(graf)
        slownik = {x: graf.pobierzWartoscF(self.pobierzAktualnyWierzcholek(), x) for x in nieodwiedzone}
        return slownik

    def dodajWierzcholekDoSciezki(self, graf):
        losowa = random.random()
        wartosciFeromonowNieodwiedzonychSasiadow = self.pobierzFeromonySasiadow(graf)
        if losowa<self.pvalue:
            maxValue = max(wartosciFeromonowNieodwiedzonychSasiadow.values())
            for key, value in wartosciFeromonowNieodwiedzonychSasiadow.values():
                if value == maxValue:
                    maxArg = key
            self.sciezka.append(maxArg)
        else:
            argumenty = self.pobierzListeNieodwiedzonychWierzcholkow(graf)
            zmiennaLosowaS = self.stworzZmiennaLosowaDyskretna(argumenty,wartosciFeromonowNieodwiedzonychSasiadow,graf)
            return zmiennaLosowaS.rvs()


    def stworzZmiennaLosowaDyskretna(self, argumenty, wartosciFeromonowNieodwiedzonychSasiadow, graf):
        wartosciPrawdopodobienstw = self.wyliczWartosciPrawodpodobienstwaDlaWszystkichArgumentow(argumenty, wartosciFeromonowNieodwiedzonychSasiadow, graf)
        zmiennaLosowaS = st.rv_discrete(name="Zmienna losowa", values=(argumenty,wartosciPrawdopodobienstw))
        return zmiennaLosowaS



    def wyliczWartoscPrawdopodobienstwaDlaArgumentu(self, x, wartosciFeromonowNieodwiedzonychSasiadow, graf, mianownik):
        if (x in self.sciezka):
            return 0
        else:
            licznik = wartosciFeromonowNieodwiedzonychSasiadow[x]*((1/(graf.pobierzOdleglosc(self.pobierzAktualnyWierzcholek(),x)))**self.beta)
            return licznik/mianownik

    def wyliczMianownikWartoscPrawdopodobienstwaDlaArgumentu(self, wartosciFeromonowNieodwiedzonychSasiadow, graf):
        mianownik = 0
        for nieodwiedzony, wartoscFeromonu in wartosciFeromonowNieodwiedzonychSasiadow:
            mianownik = mianownik + wartoscFeromonu*((1/(graf.pobierzOdleglosc(self.pobierzAktualnyWierzcholek(),nieodwiedzony)))**self.beta)
        return mianownik

    def wyliczWartoscPrawdopodobienstwaDlaArgumentu(self, x, wartosciFeromonowNieodwiedzonychSasiadow, graf):
        if (x in self.sciezka):
            return 0
        else:
            licznik = wartosciFeromonowNieodwiedzonychSasiadow[x]*((1/(graf.pobierzOdleglosc(self.pobierzAktualnyWierzcholek(),x)))**self.beta)
            mianownik = self.wyliczMianownikWartoscPrawdopodobienstwaDlaArgumentu(wartosciFeromonowNieodwiedzonychSasiadow,graf)
            return licznik/mianownik


    def pobierzAktualnyWierzcholek(self):
        return self.sciezka[-1]

    def wykonajKrok(self, graf):
        self.dodajWierzcholekDoSciezki(graf)
        graf.zmodyfikujWartoscF(self.sciezka[-2],self.sciezka[-1],self.wyliczNowaWartoscFeromonu(graf.pobierzWartoscF(self.sciezka[-2],self.sciezka[-1])))

    def wyliczNowaWartoscFeromonu(self,staraWartoscFeromonu):
        nowaWartoscFeromonu = (1-self.alfa)*staraWartoscFeromonu + self.alfa*self.tau0
        return nowaWartoscFeromonu

    def wyliczWartosciPrawodpodobienstwaDlaWszystkichArgumentow(self, argumenty,
                                                                wartosciFeromonowNieodwiedzonychSasiadow, graf):
        mianownik = self.wyliczMianownikWartoscPrawdopodobienstwaDlaArgumentu(wartosciFeromonowNieodwiedzonychSasiadow,graf)
        wartosciPrawdopodobienstwa = [self.wyliczWartoscPrawdopodobienstwaDlaArgumentu(x,wartosciFeromonowNieodwiedzonychSasiadow,mianownik
                                                                                       ) for x in argumenty]
        return wartosciPrawdopodobienstwa
    def wyliczDlugoscSciezki(self, graf):
        dlugosc = 0
        for nrWierzcholka in range(len(self.sciezka)-1):
            wierzchStart = self.sciezka[nrWierzcholka]
            wierzchKonc = self.sciezka[nrWierzcholka+1]
            dlugosc = dlugosc + graf.pobierzOdleglosc(wierzchStart,wierzchKonc)
        return dlugosc

    def wyliczDlugoscCyklu(self,graf):
        if(len(self.sciezka)!= len(graf.node)):
            raise Exception("Sciezka niekompletna!")
        else:
            return self.wyliczDlugoscSciezki(graf)+graf.pobierzOdleglosc(self.sciezka[-1],self.sciezka[0])



G=nx.Graph()
l=G.adjacency_list()


