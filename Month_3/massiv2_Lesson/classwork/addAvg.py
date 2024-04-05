import os
import random 
os.system("clear")

massiv = [random.randint(10,99) for x in range(int(input("Elementlar sonini kiriting : ")))]
print(massiv)
sum,count = 0,0

for x in massiv:
    sum += x
    count += 1
avg = sum / count

for z in range(len(massiv)):
    massiv[z] += avg
print(massiv)
print("Avg = ",avg)