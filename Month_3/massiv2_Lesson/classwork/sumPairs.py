import os
import random 
os.system("clear")
massiv = [random.randint(10,99) for x in range(int(input("Elementlar sonini kiriting : ")))]
print(massiv)
for x in range(2,len(massiv) + len(massiv)//2 ,3):
    massiv.insert(x,massiv[x-2] + massiv[x-1])
print(massiv) 