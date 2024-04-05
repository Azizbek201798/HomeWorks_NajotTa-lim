# Topshiriq_7 => DONE by LeoMessi
 
# Listda bir nechta sonlarni input orqali kiriting va ushbu sonlar orasidan 1-raqami juft bo'lganlarni chiqaring.
# Input: [123, 456, 789, 852, 12, 42, 61, 369]
# Output: 456 852 42 61

import os
os.system("clear")

list1 = list(map(int,input("Elementlarni kiriting : ").split()))

# List ichidagi 1-raqami juft bo'lgan elementni chiqarish
for x in range(len(list1)):
    if int(str(list1[x])[0]) % 2 == 0:
        print(list1[x], end = " ")


