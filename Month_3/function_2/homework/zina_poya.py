import math
# Zina poya => DONE by Azizbek

# Zina poya deb shunday kubiklar to’plamiga aytiladiki, har bir yuqori qatlami, 
# quyi qatlamdan kam kubik saqlaydi. Shunday dastur tuzingki u berilgan 
# N ta kubdan nechta zina poya tayyorlash mumkin.

import os
os.system("clear")

N = int(input())
n = N
sum,k,count = 0,1,0

while True:
    sum += k
    N -= k
    k += 1
    if sum > n:
        break
    count += 1

print(count)

# print(int((math.sqrt(8*N+1) - 1)/2))
