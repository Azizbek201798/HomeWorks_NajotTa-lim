# Topshiriq_1 => DONE by LeoMessi

# Uchta bir xil uzunlikdagi listni ma'lumotlarini bitta listga birlashtirish kerak. Ya'ni 1-list ma'lumoti dictionaryning keysi bo'ladi va 
# 2-list va 3-list ma'lumotlari esa alohida dictionaryning keys va valuesi bo'ladi.
# Input:
# ['S001', 'S002', 'S003', 'S004']
# ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# [85, 98, 89, 92]
# Output:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]

import os
os.system("clear")

ls1 = ['S001', 'S002', 'S003', 'S004']
ls2 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
ls3 = [85, 98, 89, 92]

massiv = []

for x in range(len(ls1)):
    massiv.append({ls1[x]:{ls2[x]:ls3[x]}})

print(massiv)



