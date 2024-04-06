# Topshiriq_3 => Done by Azizbek

# Printer nomli class berilgan 5ta obyektli. 
#      Ma'lumotlari: (modeli, tezligi, narxi, turi,yil).
#      Kirish va chiqarish methodlari bo'lishi kerak.
#      Methodda Printerning narxi bo'yicha saralab chiqaradigan dastur tuzing va 
#      boshqa methodda kiritilgan yildagi va kiritilgan turdagi printerlar haqida ma'lumot chiqaradigan kode yozing.

import os
os.system("clear")

class Printer:
    def __init__(self, modeli:str, tezligi:int, narxi:int, turi:str, yil:int):
        self.modeli = modeli
        self.tezligi = tezligi
        self.narxi = narxi
        self.turi = turi
        self.yil = yil

    def get_info(self):
        print(f"Modeli : {self.modeli}; Tezligi : {self.tezligi}; Narxi : {self.narxi}; Turi : {self.turi}; Yil : {self.yil}")

def set_info():
        modeli = input("Modeli : ")
        tezligi = int(input("Tezligi : "))
        narxi = int(input("Narxi : "))
        turi = input("Turi : ")
        return Printer(modeli,tezligi,narxi,turi)

def sort_by_price(a : list):
    return sorted(a,key = lambda x : x.narxi)

def show_info(year : int,tur : str, printer : Printer):
    if printer.yil == year and  printer.turi == tur:
        return printer

# Task - 1 : Whileda Printer obyektini listga kiritish:

# printers,op = [],1
# while op == 1:
#     os.system("clear")
#     printer = set_info()
#     printers.append(printer)
#     op = int(input("Yana printer qo'shmoqchimisiz? 1. Ha 0. Yo'q => "))

# os.system("clear")
# for x in printers:
#     x.get_info()

# Task - 2 : Narx bo'yicha saralash:

# printers = [Printer("HP      ",450,500," Rangli"),
#             Printer("Samsung ",250,400," Oq-qora"),
#             Printer("Artel   ",100,250," Lazerli"),
#             Printer("Siemens ",900,1500,"3 talik"),
#             Printer("Win     ",330,550," Rangli"),]

# result = sort_by_price(printers)

# os.system("clear")
# for x in result:
#     x.get_info()

# Task - 3:
# Ma'lumotni kiritilgan yil va turi bo'yicha tekshirib chiqarish

# printers = [Printer("HP      ",450,500," Rangli",2024),
#             Printer("Samsung ",250,400," Oq-qora",2010),
#             Printer("Artel   ",100,250," Lazerli",1998),
#             Printer("Siemens ",900,1500,"3 talik",2000),
#             Printer("Win     ",330,550," Rangli",2005)]
# for x in printers:
#    res = show_info(2024,"Rangli",x)
#    res.get_info()