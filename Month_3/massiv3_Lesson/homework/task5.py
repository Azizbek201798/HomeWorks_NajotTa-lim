# Topshiriq_5 => DONE by LeoMessi

# Listda bir nechta sonlar kiritilgan va sizning vazifangiz ushbu sonlardan eng katta son yasash.
# Input (Kiruvchi maâ€™lumotlar):
# [1, 2, 3]
# [61, 228, 9]
# Output (Chiquvchi maâ€™lumotlar): 
# 321
# 961228

import os
os.system("clear")

list1 = list(map(int,input("Massiv elementlarini kiriting : ").split()))

# Listning elementlarini [0] indeksiga ko'ra sortlash;
for i in range(len(list1)):
    for j in range(1,len(list1)):
        if int(str(list1[j-1])[0]) < int(str(list1[j])[0]):
            temp = list1[j-1]
            list1[j-1] = list1[j]
            list1[j] = temp

number = ""
# Listning elementlaridan eng katta son hosil qilib chiqarish;
for x in list1:
    number += str(x)

print(f"Eng katta son = {int(number)}")

