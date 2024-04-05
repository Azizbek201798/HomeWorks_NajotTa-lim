# Topshiriq_5 => DONE by LeoMessi
#  Input orqali kiritilgan string ma'lumotlarni tuplega bittalab joylashtiring. 
# Input: python 3.0
# Output: ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')

import os
os.system("clear")

word = input("Ixtiyoriy so'z kiriting : ")
mine = word.split()

massiv = tuple()
massiv = list(massiv)

# Filling tuple with letters:
for z in mine:
    for k in z:
        massiv.append(k)

massiv = tuple(massiv)
print(massiv)