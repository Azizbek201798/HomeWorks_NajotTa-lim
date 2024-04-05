import os
import random
os.system("clear")

N = int(input("N = "))
massiv = []

# Input random number to slice
while(N > 0):
    massiv.append(random.randint(10,99))
    N -= 1

# Check
for x in range(2, len(massiv)+len(massiv)//2, 3):
    massiv.insert(x, massiv[x-2] + massiv[x-1])
print(massiv)
