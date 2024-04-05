# Topshiriq_2***
# a dan b sonigacha toq sonlarlarni teskari tartibda listga joylashtirish.
# Input: a=10 b=20
# Output: sonlar=[19,17,15,13,11]

import os
os.system("clear")

a = int(input("a = "))
b = int(input("b = "))

massiv = list()

if a % 2 != 0:
    a = a 
else :
    a += 1

for x in range(a,b+1,2):
    massiv.append(x)
massiv.reverse()
print(massiv)
