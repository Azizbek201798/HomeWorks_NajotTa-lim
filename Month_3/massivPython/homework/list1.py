# Topshiriq_1***
# a dan b sonigacha juft sonlarlarni to'g'ri tartibda listga joylashtirish.
# Input: a=10 b=20
# Output: sonlar=[10,12,14,16,18]

import os
os.system("clear")

ruyxat = list()
a = int(input("a = "))
b = int(input("b = "))

if a % 2 == 0:
    a = a
else :
    a = a + 1

for x in range(a,b+1,2):
    ruyxat.append(x)
print(ruyxat)
