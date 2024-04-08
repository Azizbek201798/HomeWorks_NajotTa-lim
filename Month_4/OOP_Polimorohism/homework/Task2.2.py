# Task - 2.2 => DONE by Azizbek
 
# Method override bo'yicha 2 ixtiyoriy dastur yozing (class nomi ixtiyoriy) 

import os
os.system("clear")

class Hayvon:
    def __init__(self):
        self.name = None
        self.weight = None
        self.height = None
        self.country = None
    
    def print_info(self):
        print(f"Hayvonlar nomi,ogirligi,bo'yi,mamlakatiga ko'ra farqlanadi!")
    
class Toshbaqa(Hayvon):
    def __init__(self):
        super().__init__()
        self.set_info()

    def set_info(self):
        self.name = "Toshbaqa"
        self.weight = 12.25
        self.height = 0.2
        self.country = "Ispaniya"
    
    def print_info(self):
        print(f"Nomi : {self.name} Ogirligi : {self.weight} Bo'yi : {self.height} Mamalakat : {self.country}")
    
class Sher(Hayvon):
    def set_info(self):
        self.name = "Sher"
        self.weight = 45
        self.height = 1
        self.country = "Afrika"
    
    def print_info(self):
        print(f"Nomi : {self.name} Ogirligi : {self.weight} Bo'yi : {self.height} Mamalakat : {self.country}")

if __name__ == "__main__":
    
    toshbaqa1 = Toshbaqa()
    sher1 = Sher()

    sher1.set_info()
    sher1.print_info()
    print("\n*******************************\n")
    toshbaqa1.print_info()