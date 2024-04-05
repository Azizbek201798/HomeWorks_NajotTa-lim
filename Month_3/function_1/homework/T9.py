# T9 => DONE by Azizbek

# Ichma ich list qabul qiluvchi va quyidagicha dictionary qaytaruvchi function tuzing
# Input:
# [
# [1, 'Jean Castro', 'V'],
# [2, 'Lula Powell', 'V'],
# [3, 'Brian Howell', 'VI'],
# [4, 'Lynne Foster', 'VI'],
# [5, 'Zachary Simon', 'VII']
# ]
# Output:
# {
# 1: ['Jean Castro', 'V'],
# 2: ['Lula Powell', 'V'],
# 3: ['Brian Howell', 'VI'],
# 4: ['Lynne Foster', 'VI'],
# 5: ['Zachary Simon', 'VII']
# }

import os
os.system("clear")

ls1 = [[1, 'Jean Castro', 'V'],[2, 'Lula Powell', 'V'],[3, 'Brian Howell', 'VI'],[4, 'Lynne Foster', 'VI'],[5, 'Zachary Simon', 'VII']]
print(f"Before : {ls1}")

def changeToDict(k : list):
    dc1 = {}
    for x in range(len(k)):
        dc1.update({k[x][0] : [ k[x][1], k[x][2] ]})

    return dc1

dcNew = changeToDict(ls1)
print(f"After  : {dcNew}")

