import os
import random
os.system("clear")

N = int(input("Elementlar sonini kiriting : "))
massiv = []

# Input massiv with random numbers
for x in range(N):
    massiv.append(random.randint(10,99))
print(f"Massiv elementlari : {massiv}")
index,max = 0,0

for x in range(1,N):
    if massiv[x-1] + massiv[x] > max:
        max = massiv[x-1] + massiv[x]
        index = x-1
print(f"Yigindisi eng katta bo'lgan elementlar => {massiv[index]},{massiv[index+1]}, sum = {massiv[index] + massiv[index+1]} ")
