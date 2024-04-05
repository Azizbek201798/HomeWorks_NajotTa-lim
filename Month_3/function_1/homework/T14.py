# T14 => DONE by Azizbek 

# Sizga list berilgan. Listdagi o'sish tardibida kelgan sonlar to'plamlar sonini hisoblab qaytaruvchi funktsiya yozing. 
# Input:
# [1, 3, 4, 9, 3, 4, -1, 7, 8 ]
# Output:
# 3
# Masalan lst = [1, 3, 4, 9, 3, 4, -1, 7, 8 ]
# Bu listda o'sish tardibida kelgan to'plamlar bu 
# " 1, 3, 4, 9 "
# " 3, 4 "
# " -1, 7, 8 "
# Ularning soni 3ta

import os
os.system("clear")

ls1 = list(map(int,input("List elementlarini kiriting : ").split()))
print(f"Input  : {ls1}")

def countIncrement(l : list):
    count = 0
    for x in range(1,len(l)):
        if l[x-1] > l[x] or x == len(l) - 1:
            count += 1
    return count

res = countIncrement(ls1)
print(f"Output : {res}")


