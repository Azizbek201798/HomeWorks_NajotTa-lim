import os
from abc import ABC, abstractmethod

os.system("clear")

class Transport(ABC):
    
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Transport):
    def go(self):
        print("You are in a car!")

class MotoBike(Transport):
    def go(self):
        print("You are in a Motor bike!")

transport = Transport()
car = Car()
motobike = MotoBike()

transport.go()
car.go()
motobike.go()