# P2:

# Listning oxirgi elementini boshqa listga o'zgartirib qo'ying.

# Input:
# [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]

# Output:
# [1, 3, 5, 7, 9, 2, 4, 6, 8]

ls1 = [1, 3, 5, 7, 9, 10]
ls2 = [2, 4, 6, 8]

ls1.remove(ls1[len(ls1) - 1])
ls1.extend(ls2)
print(ls1)