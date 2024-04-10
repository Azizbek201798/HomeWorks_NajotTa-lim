import os
from uuid import uuid4
os.system("clear")

# print(uuid4()) -> takrorlanmaydigan id;

class Avto:
    def __init__(self,nomi,price,__id,__km = 0):
        self.nomi = nomi
        self.price = price
        self.__id = __id
        self.__km = __km
    
    def __str__(self):
        return f"{self.nomi} {self.price} {self.__km} {self.__id}"

    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id
    
avto1 = Avto("Lambarjini",200000,uuid4())
print(avto1.get_id())
