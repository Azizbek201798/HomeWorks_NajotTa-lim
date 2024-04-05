import os
import random
os.system("clear")

N = int(input("Elementlar sonini kiriting : "))
massiv = list()

for i in range(N):
    massiv.append(random.randint(10,99))

max = massiv[0]
print(f"Juft indexli qiymatlar : {max}",end = ",")
for i in range(2,N,2):
    print(f"{massiv[i]}",end = ",")
    if max < massiv[i]:
        max = massiv[i]
print(f"\nJuft indexli elementlardan eng kattasi = {max}")    

