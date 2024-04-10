import os
from uuid import uuid4
os.system("clear")

class Avto:
    def __init__(self,make : str, model : str, prise : int, __km,__id):
        self.make = make
        self.model = model
        self.prise = prise
        self.__km = __km
        self.__id = __id
    
    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id

    def add_km(self,km : int):
        if km >= 0:
            self.__km += km
        else :
            print("Km ni qiymatini kamaytirib bo'lmaydi!")

avto1 = Avto("Tesla","X - space",200000,1000,uuid4())
# print(avto1.make)
# print(avto1.model)
# print(avto1.prise)
# print(avto1.get_km())
print(type(avto1.get_id()))
# print(avto1.add_km(1000))
# print(avto1.get_km())