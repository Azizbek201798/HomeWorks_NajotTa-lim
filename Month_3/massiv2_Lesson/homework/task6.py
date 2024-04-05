# Topshiriq_6 => DONE by LeoMessi
# List ichida tuple berilgan va ushbu tuplening min va max qiymatlarini almashtiring.
# Input: [(10, 20, 40), (55, 50, 60), (70, 8, 9)]
# Ouput: [(40,20,10),(55,60,50),(8,70,9)]

import os
import random
os.system("clear")

n = int(input("Tuple elementlari sonini kiriting : "))
k = int(input("List  elementlari sonini kiriting : "))
massiv = [tuple(random.randint(10,99) for x in range(n)) for y in range(k)]
print(f"Before massiv : {massiv}")

for x in range(len(massiv)):
    massiv[x] = list(massiv[x])
    max = massiv[x][0]
    min = massiv[x][0]
    for y in range(1,len(massiv[x])):
        if massiv[x][y] >= max:
            max = massiv[x][y]
        elif massiv[x][y] < min:
            min = massiv[x][y]
    for z in range(len(massiv[x])):
        if massiv[x][z] == max:
            massiv[x][z] = min
        elif massiv[x][z] == min:
            massiv[x][z] = max
    massiv[x] = tuple(massiv[x])

print(f"After  massiv : {massiv}")
