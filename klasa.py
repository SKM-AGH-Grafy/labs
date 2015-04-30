__author__ = 'kuban'

class Person(object):
    ID = 0                            # zmienna statyczna
    def __init__(self, name, age=0):
        self.name = name
        self.age  = age
        print("osoba - konstruktor")
    def lastName(self):
        return self.name.split()[-1]
    def __str__(self):
        return "{}({},{})".format(self.__class__.__name__,
                                  self.name, self.age)
    def nowa_metoda(self):
        print(self.name3)

class Osobadziwna(Person):
    def __init__(self):
        self.name3 ="yy"

a=Person("Janusz")
a.name7=8
print(a.name7)
osobadziwna = Osobadziwna()
Person.nowa_metoda(osobadziwna)
#print(osobadziwna.name)