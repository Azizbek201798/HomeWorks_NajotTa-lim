# Topshiriq_1 => DONE BY Azizbek

#  Hayvon nomli class berilgan va uning 2ta voris bo'lib keladigan classlari bor(1-class Yirtqichlar, 2-class O'txo'rlar). 
#  Har bir voris bo'lgan classlar uchun 3tadan xususiyat(method) yarating (masalan, tish yirtqichlar uchun go'sht yeyish uchun kerak,
#  tish o'txo'rlar uchun o't yeyish uchun kerak )

import os
os.system("clear")

class Hayvon:
    def __init__(self,nomi:str = "Bo'ri",age:int = 25, tooth:bool = True,speed:int = 30, movement:str = "Yuguradi",size: float = 2.15):
        self.nomi = nomi
        self.age = age
        self.tooth = tooth
        self.speed = speed
        self.size = size
        self.movement = movement

    def get_age(self):
        return self.age
    
    def get_speed(self):
        return self.speed

    def get_tooth(self):
        return self.tooth
    
    def get_speed(self):
        return self.speed
    
    def get_movement(self):
        return self.movement

    def get_size(self):
        return self.size
    
class Yirtqichlar(Hayvon):
    def __init__(self,nomi = "Ayiq",soni = 45,tooth = True, speed = 45.87):
        super().__init__(tooth,speed)
        self.nomi = nomi
        self.soni = soni

    def get_info(self):
        print(f"Nomi : {self.nomi}; Soni : {self.soni}; Tish : {self.tooth}; Tezlik : {self.speed};")

class Otxorlar(Hayvon):
    def __init__(self,nomi = "Xo'roz",country = "Tatariston",movement = "Yuradi,yuguradi",size = 1.76):
        super().__init__(size)
        self.nomi = nomi
        self.country = country
        self.movement = movement

    def get_info(self):
        print(f"Nomi : {self.nomi}; Country : {self.country}; Movement : {self.movement}; Size : {self.size}")

    def get_size(self):
        return self.size
    
hayvon = Hayvon("Bo'ri", 50, True, 30, "Yuguradi", 3.15)

yirtqich1 = Yirtqichlar("Yo'lbars",65)
yirtqich1.get_info()
print("Tezlik :",yirtqich1.get_speed())
print("Movement :",yirtqich1.get_movement())

print("--------------------------------")

otxor1 = Otxorlar("O'rdak","Uzbekistan")
otxor1.get_info()
print("Movement :",otxor1.get_movement())
print("Size :",otxor1.get_size())