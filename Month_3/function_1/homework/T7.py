# T7 => DONE BY Azizbek

# Uchta list ni quyidagicha birlashtiruvchi function tuzing:
# Input:
# ['S001', 'S002', 'S003', 'S004']
# ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# [85, 98, 89, 92]
# Output:
# [
# {'S001': {'Adina Park': 85}},
# {'S002': {'Leyton Marsh': 98}},
# {'S003': {'Duncan Boyle': 89}},
# {'S004': {'Saim Richards': 92}}
# ]

# Note: natijada list ichida dictionary lar xosil bo'lgan

import os
os.system("clear")

ls1 = ['S001', 'S002', 'S003', 'S004']
ls2 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
ls3 = [85, 98, 89, 92]
ls4,ls_total = [],[]

def change(x : list, y : list, z : list):
    for a in range(len(ls1)):
        ls4.append({ls2[a] : ls3[a]})

    for b in range(len(ls1)):
        ls_total.append({ls1[b] : ls4[b]})

change(ls1,ls2,ls3)
print(ls_total)
