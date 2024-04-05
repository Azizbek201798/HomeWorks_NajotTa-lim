# Topshiriq_12 => DONE by LeoMessi

#  List ichidagi har bir tuple ma'lumotlarni yig'indisini listga joylashtiring.
# Input:
# [(1, 2), (2, 3), (3, 4)]
# Output:
# [3, 5, 7]
# Input:
# [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
# Output:
# [9, -1, 7, 8] 

import os
os.system("clear")

list1 = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
list2 = []
print(f"List1 : {list1}")

for x in list1:
    list2.append(sum(list(x)))

print(f"List2 : {list2}")
