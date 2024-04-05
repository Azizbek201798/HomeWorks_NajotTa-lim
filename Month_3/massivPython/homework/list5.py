# Topshiriq_5***
# n ta dastlabki fibonachchi sonlaridan List hosil qiling va ushbu list elementlarini yig'indisini chiqaring:
# Input:  n = 5
# Outpt:  ls = [0 , 1 , 1 , 2 , 3 ]  sum = 7
import os
os.system("clear")

fb1,fb2,f3 = 0,1,None
massiv = list()
massiv.append(fb1)

N = int(input("Elementlar sonini kiriting(N > 0) : "))
sum = 0

if  N <= 0:
    print("Elementlar soni manfiy yoki 0 bo'lmaydi!")
elif N < 2:
    print(massiv)
    sum += fb1
elif N < 3:
    massiv.append(fb2)
    print(massiv)
    sum = fb1 + fb2     
elif N >= 3:
    for x in range(N-1) :
        fb3 = fb1+fb2
        massiv.append(fb3)
        fb1 = fb2
        fb2 = fb3
        sum += fb3
    print(massiv)
    print(f"Elementlar yig'indisi = {sum}")

