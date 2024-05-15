# TASK - 3 => DONE by Azizbek

# Vehicle nomli abstract class yarating. Ushbu class tarkibida StartEngine()  va StopEngine() abstract methodlarini hosil qiling.
# Vehicle sinfidan Car va Motorcycle nomli subclasslarni hosil qiling. Har bir transport turi uchun divigatelni ishga 
# tushish(StartEngine()) va to'xtashi (StopEngine()) methodlarini yozing.

import os
from abc import ABC,abstractmethod
os.system("clear")

class Vehicle(ABC):
    
    @abstractmethod
    def StartEngine(self):
        print("Bu mashinani o't oldiruvchi metod!")

    @abstractmethod
    def StopEngine(self):
        print("Bu mashinani o't o'chiruvchi metod!")

class Car(Vehicle):

    def StartEngine(self):
        return "Mashina o't oldi!"
    
    def StopEngine(self):
        return "Mashina o'chirildi!"

class Motorcycle(Vehicle):

    def StartEngine(self):
        return "Matotsikl o't oldi!"
    
    def StopEngine(self):
        return "Matatsikl o'chirildi!"

car = Car()
print(car.StartEngine())
print(car.StopEngine())

print("************************")

motorcycle = Motorcycle()
print(motorcycle.StartEngine())
print(motorcycle.StopEngine())