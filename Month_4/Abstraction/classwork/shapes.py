import os
import math
from abc import ABC, abstractmethod
os.system("clear")

class Shakl(ABC):
    @abstractmethod
    def Yuza(self):
        print("Bu yuzani topuvchi method!")
    
    @abstractmethod
    def Perimetr(self):
        print("Bu perimetrni topuvchi method!")

class Tortburchak(Shakl):
    def __init__(self):
        self.a = 10
        self.b = 20

    def Yuza(self):
        return self.a * self.b

    def Perimetr(self):
        return 2*(self.a + self.b)

class Doira(Shakl):
    def __init__(self):
        self.r = 10

    def Yuza(self):
        return math.pi * self.r ** 2

    def Perimetr(self):
        return 2 * math.pi * self.r

tortbuchak = Tortburchak()
print("Tortburchak yuzi : ",tortbuchak.Perimetr())
print("To'rtburchak perimetr : ",tortbuchak.Yuza())

print("\n**********************************************\n")

doira = Doira()
print("Doira yuzi : ",int(doira.Yuza()))
print("Doira perimetr ",int(doira.Perimetr()))