# Topshiriq_5 => DONE by Azizbek

#  Kompyuter nomli class berilgan. Ushbu classning elementlari quyidagicha: 
# 1) Kompyuter nomi; 2) Kompyuter RAMI; 3) Kompyuter narxi; 
# 4) Kompyuter protsessori;
# Bu classda kiritish va chiqarish methodlarini ishlating. 4ta obyektlar 
# ichidan RAMi 4dan ko'p va 16dan kichik obyektlar haqida ma'lumot chiqaring.
import os
os.system("clear")

class Kompyuter:
    def __init__(self,nomi,RAM,narxi,protsessori):
        self.nomi = nomi
        self.RAM = RAM
        self.narxi = narxi
        self.protsessori = protsessori
    
    def set_info(self):
        nomi = input("Nomi : ")
        RAM = int(input("RAM : "))
        narxi = input("Narxi : ")
        protsessori = input("Protsessori : ")
        return Kompyuter(nomi,RAM,narxi,protsessori)
    
    def get_info(self):
        print(f"Nomi : {self.nomi}; RAM : {self.RAM}; Narxi : {self.narxi}; Protsessori : {self.protsessori}")

# TASK - 1: Kiritish va chiqarish metodlarini ishlatish:

# op,kompyuterlar = 1,[]

# while op :
#     os.system("clear")
#     kompyuter = Kompyuter("Acer",16,400,"CPU").set_info()
#     kompyuterlar.append(kompyuter)
#     op = int(input("Yana ma'lumot qo'shasizmi? 1.Ha 2.Yo'q : "))

# os.system("clear")
# for x in kompyuterlar:
#     x.get_info()

# TASK - 2: 4ta obyektlar ichidan RAMi 4dan ko'p va 16dan kichik obyektlar haqida ma'lumot chiqaring.

# kopmyuterlar = [Kompyuter("Acer  ",8,360,"CPU"),
#                 Kompyuter("HP    ",16,1000,"CPU"),
#                 Kompyuter("Victus",32,1500,"CPU"),
#                 Kompyuter("MAC 1 ",2,500,"CPU")]

# for x in kopmyuterlar:
#     if x.RAM >= 4 and x.RAM <= 16:
#         x.get_info()