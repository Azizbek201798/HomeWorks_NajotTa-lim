import os
import random
os.system("clear")

N = int(input("Elementlar sonini kiriting : "))
massiv = list()

for i in range(N):
    massiv.append(random.randint(10,99))
print(massiv)
search = int(input("Son kiriting : "))
index, near = 0, abs(massiv[0] - search)

for i in range(1,N):
    if abs(massiv[i] - search) <= near:
        index = i
        near = abs(massiv[i] - search)
print(f"Kiritilgan songa eng yaqini = {massiv[index]}") 
