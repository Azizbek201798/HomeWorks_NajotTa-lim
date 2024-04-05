import os
import random
os.system("clear")

massiv = [random.randint(10,14) for x in range(int(input("Elementlar sonini kiriting : ")))]
print(massiv)

while True:
    check = True
    for z in range(1,len(massiv)):
        if massiv[z-1] == massiv[z]:
            massiv.pop(z)
            check = False
            break
    if check == True:
        break
print(massiv)