# Topshiriq_13 => DONE by LeoMessi

# Listning ichidagi tuple ma'lumotlarni listga o'girib beradigan dastur tuzing.
# Input: [(1, 2), (2, 3), (3, 4)]
# Output: [[1, 2], [2, 3], [3, 4]]
# Input: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
# Output: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]

import os
os.system("clear")

list1 = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
list2 = []

print(f"List1 : {list1}")

for x in list1:
    list2.append(list(x))

print(f"List2 : {list2}")
