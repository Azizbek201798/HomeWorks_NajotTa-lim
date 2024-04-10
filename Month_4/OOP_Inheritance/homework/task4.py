# Topshiriq_4 => DONE by Azizbek

#  Kitob nomli class berilgan. Ushbu classning elementlari quyidagicha: 
# 1) Kitob nomi; 2) Kitob mualliflari; 3) Kitob narxi; 4) Kitob nashriyoti;
# Bu classda kiritish va chiqarish methodlarini ishlating. 
# 5ta obyektlar ichidan Kitob nashriyoti Alfavitning A harfidan
# H gacha bo'lgan harflar bilan boshlanadigan obyektlar haqida ma'lumot chiqaring.

import os
os.system("clear")

class Kitob:
    def __init__(self,nomi : str,muallifi : str,narxi : int,nashriyot : str):
        
        self.nomi = nomi
        self.muallifi = muallifi
        self.narxi = narxi
        self.nashriyoti = nashriyot
    
    def set_info(self):
        
        nomi = input("Nomi : ")
        muallifi = input("Muallifi : ")
        narxi = int(input("Narxi : "))
        nashriyot = input("Nashriyot : ")

        return Kitob(nomi,muallifi,narxi,nashriyot)

    def get_info(self):
        print(f"{self.nomi};{self.muallifi};{self.narxi};{self.nashriyoti}")

# TASK - 1: Kiritish va chiqarish methodini ishlatilishi namunasi:

# op,kitoblar = 1,[]
# while op:
#     os.system("clear")
#     kitob = Kitob("Qafas","Kamola Almirzayeva",1000000,"Uyda")
#     kitoblar.append(kitob.set_info())
#     op = int(input("Ya'na ma'lumot kiritasizmi ? 1. Ha 2. Yo'q : "))

# for x in kitoblar:
#     x.get_info()

# TASK - 2: Agar Nashriyot A harfidan H gacha bo'lgan harflardan boshlangan bo'lsa chiqaring  

# kitoblar = [Kitob("Sariq devni minib!","Xudoyberdi To'xtaboyev",200000,"Hilol"),
#             Kitob("Vatan","Abdulla Oripov",300000,"Sayr"),
#             Kitob("Xalqim","Azizbek Ziyodullayev",500000,"Uyda"),
#             Kitob("Barselona tarixi","Leo Messi",150000,"Cataloniya"),
#             Kitob("Chelsi","Lampard",123456,"London")] 

# os.system("clear")
# for x in kitoblar:
#     if ord(x.nashriyoti[0]) >= 65 and ord(x.nashriyoti[0]) <= 72:
#         x.get_info()
