# TASK - 4 => DONE by Azizbek 

# Bird nomli abstract classni hosil qiling. Ushbu class tarkibida fly() va makeSound() nomli abstract methodlarni yarating. 
# Yuqoridagi abstract sinfdan Eagle va Hawk nomli voris sinflarni hosil qiling.  Har bir qush uchun yuqorida berilgan 
# abstract methodlar (fly(),makeSound()) uchun uchish va ovozlarini hosil qiluvchi funksiyalar yozing. 

import os
from abc import ABC, abstractmethod
os.system("clear")

class Bird(ABC):
    
    @abstractmethod
    def Fly(self):
        return "Hayvonlarning ba'zilari ucha oladi!"
    
    @abstractmethod
    def MakeSound(self):
        return "Hayvonlarning ba'zilari ovoz chiqara oladi!"

class Eagle(Bird):

    def Fly(self):
        return "Burgut ucha oladi!"

    def MakeSound(self):
        return "Burgut ovoz chiqara oladi!"


class Hawk(Bird):

    def Fly(self):
        return "Boyog'li ucha oladi!"

    def MakeSound(self):
        return "Boyog'li ovoz chiqara oladi!"

eagle = Eagle()
print(eagle.Fly())
print(eagle.MakeSound())

print("**************************************")

hawk = Hawk()
print(hawk.Fly())
print(hawk.MakeSound())