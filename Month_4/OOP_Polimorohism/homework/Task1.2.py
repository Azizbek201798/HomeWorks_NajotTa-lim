# Task - 1.2 => DONE by Azizbek

# Method overload bo'yicha 2 ta ixtiyoriy dastur yozing (class nomi ixtiyoriy) 

import os
import math
os.system("clear")

# SECOND EXAMPLE:

class Kub:
    def __init__(self,a,b,h):
        self.a = a
        self.b = b
        self.h = h
    
    def get_hajm(self):
        return self.a * self.b * self.h
    
class Shar:
    def __init__(self,r):
        self.r = r
    
    def get_hajm(self):
        return (4 / 3) * self.r ** 3 * math.pi

if __name__ == "__main__":
    kub1 = Kub(1,1,1)
    kub1.__init__(3,4,5)

    shar1 = Shar(1)
    shar1.__init__(5)

    shakllar = [kub1,shar1]
    for x in shakllar:
        print(f"Hajm = ",x.get_hajm())