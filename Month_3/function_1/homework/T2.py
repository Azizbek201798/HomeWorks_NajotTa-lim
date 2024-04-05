# T2 => DONE by Azizbek

# a dan b gacha sonlarni ekranga chiqaradigan recursive function tuzing. Faqat, a >= b dan bo'lgan holatlar uchun\
# Input: 7 2
# Output: 7 6 4 5 3 2

import os
os.system("clear")

a,b = map(int,input("a,b = ").split())

def myFunction(a : int, b : int):
    if (a < b):
        return

    print(f"{a} ",end = " ")
    myFunction(a-1,b)

myFunction(a,b)
