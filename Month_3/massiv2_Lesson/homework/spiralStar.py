# For Me

import os
os.system("clear")

n,my,your = int(input("n = ")),1,0
rowMin, rowMax, colMin, colMax = 0, n-1, 0, n-1
massiv = [[0] * n for x in range(n)]

while rowMin <= rowMax and colMin <= colMax:
    
    for i in range(colMin,colMax+1):
        massiv[rowMin][i] = 1
    rowMin += 1

    for i in range(rowMin,rowMax+1):
        massiv[rowMin][i] = 1
    colMax -= 1

    for i in range(colMax,colMin-1,-1):
        massiv[rowMin][i] = 1
    rowMax -= 1

    for i in range(rowMax,rowMin-1,-1):
        massiv[rowMin][i] = 1
    colMin += 1

# Show massiv
for x in range(n):
    for y in range(n):
        print("{:4d}".format(massiv[x][y]),end = "")
    print("\n")

#  1 1 1 1 1 1 
#  0 0 0 0 0 1
#  1 1 1 1 0 1
#  1 0 1 1 0 1
#  1 0 0 0 0 1
#  1 1 1 1 1 1



