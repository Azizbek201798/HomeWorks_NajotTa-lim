import os
import random
os.system("clear")

N = int(input("N = "))
massiv = []
while(N > 0):
    massiv.append(random.randint(10,99))
    N -= 1
print(massiv)