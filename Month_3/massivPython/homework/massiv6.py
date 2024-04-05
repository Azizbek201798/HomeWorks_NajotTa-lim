import os 
import random
os.system("clear")

N = int(input("Elementlar sonini kiriting : "))
massiv = list(())

for i in range(N):
    massiv.append(random.randint(10,99))
print(massiv)
local_max,max = None,None
print("Lokal ekstriumlar = ",end = " ")

for x in range(2,len(massiv)):
    if massiv[x-1] > massiv[x-2] and massiv[x-1] > massiv[x]:
        local_max = massiv[x-1]
        print(f"{local_max}",end = ",")
    if max is None:
        max = local_max
    elif max < local_max:
        max = local_max    
if local_max is None :
    print("Massiv local ekstriumga ega emas!")
else :
    print(f"\nLocal ekstriumlardan eng kattasi = {max}")
