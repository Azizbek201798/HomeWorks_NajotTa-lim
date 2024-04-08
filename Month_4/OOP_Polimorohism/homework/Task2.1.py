# Task - 2.1 => DONE by Azizbek
 
# Method override bo'yicha 2 ixtiyoriy dastur yozing (class nomi ixtiyoriy) 

import os
os.system("clear")

class Texnika:
    def __init__(self):
        self.name = None
        self.sotildi = None
        self.turi = None
        self.narxi = None
    
    def print_info(self):
        print("Texnikalar turi va narxiga ko'ra farq qiladi!")

class Nootebook(Texnika):
    def __init__(self):
        super().__init__()
        self.set_info()

    def set_info(self):
        self.name = "HP"
        self.sotildi = 10
        self.turi = "Yangi"
        self.narxi = 550
    
    def print_info(self):
        print(f"Nomi : {self.name} Sotildi : {self.sotildi} ta Turi : {self.turi} Narxi : {self.narxi}")

class Playstation5(Texnika):
    def set_info(self):
        self.name = "Playstation5"
        self.narxi = 700
        self.sotildi = 17
        self.turi = "Eski"

    def print_info(self):
        print(f"Nomi : {self.name} Sotildi : {self.sotildi} ta Turi : {self.turi} Narxi : {self.narxi}")

if __name__ == "__main__":

    notebook1 = Nootebook()
    playstation1 = Playstation5()

    playstation1.set_info()
    playstation1.print_info()
    print("\n****************************\n")
    notebook1.print_info()