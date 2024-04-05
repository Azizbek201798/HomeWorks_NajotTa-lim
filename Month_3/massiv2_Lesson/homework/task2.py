# Topshiriq_2 => DONE by LeoMessi
# List ichida tuple berilgan va ushbu tuplning oxirgi elementini 100 almashtiring.
# Input: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
import os
import random
os.system("clear")

n = int(input("Tuple elementlari sonini kiriting : "))
k = int(input("List  elementlari sonini kiriting : "))

massiv = [tuple(random.randint(10,99) for x in range(n)) for z in range(k)]

print(f"Before massiv : {massiv}")

for x in range(len(massiv)):
    massiv[x] = list(massiv[x])
    massiv[x][n-1] = 100
    massiv[x] = tuple(massiv[x])
print(f"After  massiv : {massiv}")