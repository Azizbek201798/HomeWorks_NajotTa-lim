# Topshiriq_11 => DONE by LeoMessi

# Dictionary ma'lumotlarini input orqali kiriting. Ushbu dictionaryda eng katta 3ta qiymatli kalitlarni chiqaring.
# Input: n = 5 dict1={1: 123, 2: 456, 3:231, 4:789, 5:654}
# Output: 2 4 5

import os
os.system("clear")

n = int(input("n = "))
dict1 = {}

while n > 0:
    key   = input("Key : ")
    value = input("Value : ")
    dict1.update({int(key):int(value)})
    n -= 1

list1 = list(dict1.values())
k,x = len(list1),1
count = None

print("\nEng katta qiymatga ega keylar : ",end = " ")

for k in range(3):
    for x in dict1:
        if dict1[x] == max(list1):
            print(f"{x}",end = " | ")
            list1.remove(max(list1))
            break

print("\n")

