# Topshiriq_2 => DONE by Azizbek

# 1-klass listga faqat int ma'lumotlarni kiritishi kerak, 
# 2-klass listga faqat int yoki float ma'lumotlarni kiritishi kerak, 
# 3-klass listga faqat int yoki float yoki bool ma'lumotlarni kiritishi kerak, 
# 4-klass listga faqat int yoki float yoki bool yoki str ma'lumotlarni kiritishi kerak. 
# (Vorislikni va super methodini ishlatish kerak)

import os
os.system("clear")

class Tortinchi:

    def __init__(self, son : int = 27, pul :float = 1.25, soz : str = "Azizbek", check : bool = True):
        self.son = son
        self.pul = pul
        self.soz = soz
        self.check = check
    
    def get_info(self):
        print(f"{self.son};{self.pul};{self.soz};{self.check}")
    
class Uchinchi(Tortinchi):
    def __init__(self, son : int = 17, pul :float = 3.33, check : bool = False):
        super().__init__(son,pul,check)

    def get_info(self):
        print(f"{self.son};{self.pul};{self.check}")

class Ikkinchi(Tortinchi):
    def __init__(self, son : int = 98, pul : float = 2.22):
        super().__init__(son,pul)
    
    def get_info(self):
        print(f"{self.son};{self.pul}")

class Birinchi(Tortinchi):
    def __init__(self, son : int = 62):
        super().__init__(son)

    def get_info(self):
        print(f"{self.son}")

massiv = []

tortinchi_1 = Tortinchi(27,1000,"Azizbek",True)
massiv.append(tortinchi_1)
uchinchi_1  = Uchinchi(12,1300.65,False)
massiv.append(uchinchi_1)
ikkinchi_1  = Ikkinchi(25,6500,True)
massiv.append(ikkinchi_1)
birinchi_1  = Birinchi(13,22,False)
massiv.append(birinchi_1)

for x in massiv:
    x.get_info()

