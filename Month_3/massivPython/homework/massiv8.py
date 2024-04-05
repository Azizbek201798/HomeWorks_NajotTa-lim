import os
import random
os.system("clear")

N = int(input("Elementlar sonini kiriting : "))
massiv = []

# Input with random numbers
for i in range(N):
    massiv.append(round(0.4567*random.randint(10,99),2))
print(f"\nOld Massiv : {massiv}")

# Sort 
tepm = None
for x in range(len(massiv)):
    for y in range(1,len(massiv) - x):
        if massiv[y-1] < massiv[y]:
            temp =  massiv[y-1]
            massiv[y-1] = massiv[y]
            massiv[y] = temp

print("\nNewMassiv : ",massiv)

# PASTDA tayyor funksiyalarda foydalangan holda isglanishi keltirilgan!

# massiv.sort()
# massiv.reverse()
# print("\nNewMassiv : ",massiv)