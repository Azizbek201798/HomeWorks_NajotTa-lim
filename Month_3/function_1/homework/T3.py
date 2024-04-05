# T3 => DONE by Azizbek

# Function tuzing. Bu function, listning ichidagi tuple ni listga o'girib bersin.
# Input:    [(1, 2), (2, 3), (3, 4)]
# Output:   [[1, 2], [2, 3], [3, 4]]
# Input:    [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
# Output:   [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]

import os
os.system("clear")

N = int(input("Tuple qatorlari soni = "))
ls1 = []

while N > 0:
    ls1.append(tuple(map(int,input("Tupple elementlarini kiriting: ").split())))
    N -= 1

print(f"Before : {ls1}")

def change(ls1 : list):
    for x in range(len(ls1)):
        ls1[x] = list(ls1[x])

change(ls1)
print(f"After  : {ls1}")

