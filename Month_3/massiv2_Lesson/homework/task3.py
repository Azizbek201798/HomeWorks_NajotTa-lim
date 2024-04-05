# Topshiriq_3 => DONE by LeoMessi
# Listning ichida tuple ma'lumotlari berilgan va ushbu listdagi bo'sh tuplelarni o'chiring. 
# Input: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d',)]
# Output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

import os
os.system("clear")

massiv = [(), (), ('',),(), ('a', 'b'),(),(), ('a', 'b', 'c'), ('d',),(),(),()]
print(f"Before massive : {massiv}")
while True :
    check = True
    for x in range(len(massiv)):
        if len(massiv[x]) == 0:
            massiv.remove(massiv[x])
            check = False
            break
    if check == True:
        break

print(f"After  massive : {massiv}")
