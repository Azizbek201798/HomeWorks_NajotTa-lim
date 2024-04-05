# Topshiriq_9 => DONE by LeoMessi
# NxN matritsa elementlarini spiral ko'rinishida to'ldiring
# N = 4
#  1   2   3  4
# 12  13  14  5
# 11  16  15  6
# 10   9   8  7

import os
os.system("clear")

N = int(input("Elementlar sonini kiririting : "))
massiv,k = [[0] * N for x in range(N)],1
rowMin, colMin, rowMax, colMax = 0,0,N-1,N-1

while rowMin <= rowMax and colMin <= colMax:
    
    for x in range(colMin,colMax+1):
        massiv[rowMin][x] = k
        k += 1 
    rowMin += 1

    for x in range(rowMin,rowMax+1):
        massiv[x][colMax] = k
        k += 1
    colMax -= 1

    for x in range(colMax,colMin-1,-1):
        massiv[rowMax][x] = k
        k += 1
    rowMax -= 1

    for x in range(rowMax,rowMin-1,-1):
        massiv[x][colMin] = k
        k += 1
    colMin += 1
print("")

for i in range(N):
    for j in range(N):
        print("{:4d}".format(massiv[i][j]),end = "")
    print("\n") 