import os
import random
os.system("clear")

N = int(input("Elementlar soninin kiriting : "))
massiv = list()

for i in range(N):
    massiv.append(random.randint(10,99))

min = massiv[1]
print(f"Toq indexli qiymatlari : {min}",end = ",")

for x in range(3,N,2):
    print(f"{massiv[x]}",end = ",")
    if massiv[x] < min:
        min = massiv[x]
print(f"\nToq indexli qiymatlardan eng kichigi = {min}")