# Raqamlar yigʻindisi : DONE by Azizbek
# Sizga N soni beriladi. Ushbu sonning raqamlar yigʻindisi topishingiz kerak.

import os
os.system("clear")

N = int(input())
sum = 0
while N > 0:
    sum += N % 10
    N //= 10
print(sum)
