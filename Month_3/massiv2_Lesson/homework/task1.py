# Topshiriq_1 => DONE by LeoMessi
# Tuple e'lon qilingan va ushbu tupledagi boshidagi 4-elementni va oxirgi 4-elementni chiqaring.
# Input: t=(1,2,3,4,5,6,7,8,9,10)
# Output: 4 7

import os
import random
os.system("clear")

n = int(input("Tuple Elementlari sonini kiriting : "))
massiv = tuple(random.randint(10,99) for x in range(n))

first_ind,last_ind = 3,(len(massiv)-1)-3

print(massiv)
print(f"{massiv[first_ind]} <=> {massiv[last_ind]}")

