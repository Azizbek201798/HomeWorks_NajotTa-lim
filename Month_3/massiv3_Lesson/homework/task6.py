# Topshiriq_6 => DONE by LeoMessi

# Listni ichida list berilgan. Ichki listlar 3ta ma'lumotdan iborat. Ushbu listni dictionaryga o'tkazing.
# Input:
# [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
# Output:
# {1: ['Jean Castro', 'V'], 2: ['Lula Powell', 'V'], 3: ['Brian Howell', 'VI'], 4: ['Lynne Foster', 'VI'], 5: ['Zachary Simon', 'VII']}

import os
os.system("clear")

list1 = [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
dict1 = {}
print(f"List : {list1}")

# dict1 ga list1 dan ma'lumotlarni nusxalash
for x in range(len(list1)):
    dict1.update({list1[x][0]:[list1[x][1],list1[x][2]]})

print(f"Dictionary : {dict1}")

