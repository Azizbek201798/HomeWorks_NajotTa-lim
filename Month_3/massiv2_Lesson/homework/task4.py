# Topshiriq_4 => DONE by LeoMessi
# Listning ichida tuple ma'lumotlari berilgan va sizning vazifangiz ushbu tuplening 2-elementi bo'yicha kamayish tartibida saralash. 
# Input: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]

import os
os.system("clear")

massiv = [('item1', '12.20'), ('item2', '15.10'),('itemx','27.54'), ('item3', '24.5')]
print(f"Before massiv: {massiv}")

# Sorting DESC
for x in massiv:
    for y in range(1,len(massiv)):
        if float(massiv[y-1][1]) < float(massiv[y][1]):
            temp = massiv[y-1]
            massiv[y-1] = massiv[y]
            massiv[y] = temp

print(f"After  massiv: {massiv}")