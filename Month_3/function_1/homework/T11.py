# T11:

# List qabul qilib, listning elementlarining toq elementlarini usish tartibida, juft elementlarini kamayish tartibida 
# oz ornida tartiblab chiqaruvchi funksiya tuzing.
# Input: [1,2,3,4,5,6,7,8,9,10]
# Output:[1,10,3,8,5,6,7,4,9,2]

import os
os.system("clear")

ls1 = list(map(int,input("List elementlarini kiriting : ").split()))

def sortList(z : list):
    print(f"Before : {ls1}")
    z.sort()
    juft,toq,k = [],[],len(z)
    
    for x in z:
        if x % 2 == 0:
            juft.append(x)
        else :
            toq.append(x)
    
    z.clear()
    ind1,ind2 = 0,0
    juft.reverse()

    for x in range(k):
        if x % 2 == 0:
            z.append(toq[ind1])
            ind1 += 1
        elif x % 2 != 0:
            z.append(juft[ind2])
            ind2 += 1
    print(f"After  : {z}")

os.system("clear")
sortList(ls1)        

