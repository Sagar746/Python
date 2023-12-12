from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def noofsides(self):
        pass


class Triangle(Polygon):
    
    def noofsides(self):
        print('I have 3 sides')


class Pentagon(Polygon):
    def noofsides(self):
        print('I have 5 sides')


R = Triangle()
R.noofsides()