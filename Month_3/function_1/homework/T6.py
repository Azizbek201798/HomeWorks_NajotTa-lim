# T6 => DONE by Azizbek

# List ichidagi har bir tuple qiymatlarinig yig'indisini yangi listga joylashtiradigan funksiya yozing.
# Input:    [(1, 2), (2, 3), (3, 4)]
# Output:   [3, 5, 7]
# Input:  [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
# Output: [9, -1, 7, 8]

import os
os.system("clear")

N = int(input("Tuple qatorlari sonini kiriting : "))
ls1,lsNew = [],[]

while N > 0: 
    tp1 = tuple(map(int,input("Tuple elementlarini kiriting : ").split()))
    ls1.append(tp1)
    N -= 1

print(f"\nls1 = {ls1}")

def change(x : list):
    for x in x:
        lsNew.append(sum(list(x)))

change(ls1)
print(f"lsNew = {lsNew}")

