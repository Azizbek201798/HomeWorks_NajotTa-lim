# TASK - 2 => DONE by Azizbek

# Animal nomli abstract class hosil qiling. Class tarkibida sleep() va eat() nomli abstract methodlarni hosil qiling. 
# Animal sinfidan Tiger,Deer,Lion nomli voris sinflarni hosil qiling. Hayvonlarning tabiatiga qarab
# yuqorida berilgan abstract methodlarni qaytatdan yozing.

import os
from abc import ABC, abstractmethod
os.system("clear")

class Animal(ABC):
    def __init__(self):
        self.name = None

    @abstractmethod
    def sleep(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Tiger(Animal):
    
    def sleep(self):
        print("Tiger sleeps 10 hours a day!")
    
    def eat(self):
        print("Tiger eat meat!")
    
class Deer(Animal):

    def sleep(self):
        print("Deer sleeps 4 hours a day!")
    
    def eat(self):
        print("Deer eats grass!")

class Lion(Animal):

    def eat(self):
        print("Lion eats sheep and horse!")
    
    def sleep(self):
        print("Lion sleeps 20 hours a day!")

os.system("clear")

tiger = Tiger()
tiger.eat()
tiger.sleep()

deer = Deer()
deer.eat()
deer.sleep()

lion = Lion()
lion.eat()
lion.sleep()