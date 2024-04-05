# Topshiriq_4***
# List e'lon qilingan va ushbu listdagi boshidagi eng birinchi tub va eng oxirgi tub elementlarini chiqaring.
# Input: t=[121,12,13,4,5,6,7,8,97,10]
# Output: 13 97
import random
import os
os.system("clear")

n = int(input("Elementlar sonini kiriting : "))
massiv,primes = list(),list()
first,last = None,None

for x in range(n):
    massiv.append(random.randint(10,99))
check = None
print(massiv)

#For first Prime
for z in range(len(massiv)):
    check = True
    for x in range(2,massiv[z]):
        if massiv[z] % x == 0:
            check = False
            break
    if check == True:
        first = massiv[z]
        break

check1 = None

# For last Prime
for k in range(len(massiv) - 1,-1,-1):
    check1 = True
    for p in range(2,massiv[k]):
        if massiv[k] % p == 0:
            check1 = False
            break
    if check1 == True:
        last = massiv[k]
        break

#For all primes to check;
for z in range(len(massiv)):
    check = True
    for x in range(2,massiv[z]):
        if massiv[z] % x == 0:
            check = False
            break
    if check == True:
        primes.append(massiv[z])

print("Prime numbers : ",primes)
print(f"Boshidan Birinchi Tub = {first}")
print(f"Ohiridan Birinchi Tub = {last}")
