# T13 => DONE by Azizbek

# Funksiya orqali Listda bir nechta sonlarni input orqali kiriting va ushbu sonlar orasidan 1-raqami juft bo'lganlarni chiqaring.
# Input: [123, 456, 789, 852, 12, 42, 61, 369]
# Output: [456, 852, 42, 61]

import os
os.system("clear")

ls1 = list(map(int,input("List elementlarini kiriting : ").split()))
print(f"Input  : {ls1}")

def firstDigitEven(k : list):
    lsNew = []
    for x in k:
        if int(str(x)[0]) % 2 == 0:
            lsNew.append(x)
    print(f"Output : {lsNew}") 
    
firstDigitEven(ls1)
