# R2:

# Quyidagi arrayda sonlar berilgan. Shu arraydagi sonlarni faqat tublarini olib, prime.txt faylga yozib qo'ying.

# Array [12] = 2 19 54 23 87 41 69 84 101 57 32 17
# prime.txt: 2 19 23 41 101 17
import os
os.system("clear")
os.chdir("/home/azizbek/go/src/NajotTalim/HomeWork/Month_3/function_3/classwork")

massiv = [2, 19, 54, 23, 87, 41, 69, 84, 101, 57, 32, 17]
check = True

f = open("primes.txt","w+")
primes = []

for x in massiv:
    check = True
    for y in range(2,x):
        if x % y == 0:
            check = False
            break
    if check == True:
        primes.append(str(x) + ",")

f.writelines(primes)

data = f.read()
print(data)
