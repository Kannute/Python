from abc import ABC
from abc import abstractmethod

class Calka(ABC):

    '''Klasa bazowa dla roznych metod calkowania'''

    def __init__(self, mini, maxi, steps, function):
        self.start = mini
        self.end = maxi
        self.steps = steps
        self.fun = function
    
    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, end):
        if end < self.start :
            self.__end = self.start
            print("Bledne granice calkowania. Ustawiam gorna granice na rowna dolnej")
        else:
            self.__end = end

    @property
    def steps(self):
        return self.__steps

    @steps.setter
    def steps(self, steps):
        if steps < 1:
            self.__steps = 1
            print("Ujemna ilosc krokow. Ustawiam domyslna ilosc krokow na 1")
        else:
            self.__steps = steps

    @abstractmethod
    def calkowanie(self):

        '''Metoda calkowania, w klasie bazowej jest abstrakcyjna'''

        pass

class Trapez(Calka):

    '''Klasa pochodna klasy calka 
    zawierajaca nadpisana metode abstrakcyjna 
    obslugujaca calkowanie metoda trapezow'''

    def calkowanie(self):

        '''Calkowanie metoda trapezow'''

        h = (self.end - self.start) / self.steps
        s = 0
        for i in range(self.steps+1):
            s += self.fun(self.start + i*h) + self.fun(self.start + (i+1)*h)
        s *= (h / 2)
        return s

class Simpson(Calka):

    ''''Klasa pochodna klasy calka 
    zawierajaca nadpisana metode abstrakcyjna 
    obslugujaca calkowanie metoda Simpsona'''

    def calkowanie(self):

        '''Calkowanie metoda simsona'''

        h = (self.end - self.start) / (2*self.steps)
        s = self.fun(self.start)
    
        for i in range(1,2*self.steps):
            if(i%2 == 1):
                s += 4*self.fun(i*h)
        
        for i in range(2, 2*self.steps):
            if(i%2 == 0):
                s += 2*self.fun(i*h)
    
        s += self.fun(self.end)
        s = (h / 3)*s
        return s

from math import sin
print("Calka sinus:")
test1 = Trapez(0, 10, 1000, sin)
print("Metoda trapezow:")
print(test1.calkowanie())

test2  = Simpson(0, 10, 1000, sin)
print("Metoda Simpsona:")
print(test2.calkowanie())
