# Topshiriq_7 => DONE by LeoMessi
# List ichida tuple berilgan va elementlar yigindisi juft bo'lgan tuple elementlarini o'chiring.
# Input: [(1, 4, 2), (5, 0, 6), (7, 8, 5)]
# Ouput: [(1, 4, 2), (5, 0, 6)]

import os
import random
os.system("clear")

n = int(input("Tuple elementlarini kiriting : "))
k = int(input("List  elementlarini kiriting : "))

massiv = [tuple(random.randint(10,99) for x in range(n)) for y in range(k)]
print(f"Before massiv : {massiv}")
count = 0

while True:
    check = True
    for x in range(len(massiv)):
        sum = 0
        count += 1
        for y in range(len(massiv[x])):
            sum += massiv[x][y]
        if sum % 2 == 0:
            massiv.remove(massiv[x])
            check = False 
            break
    if check == True:
        break

print(f"After  massiv : {massiv}")
print(f"Count = {count}")