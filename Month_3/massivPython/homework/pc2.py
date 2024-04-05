import os
from random import randint
os.system("clear")

matrix = []
row = int(input("Matritsa qatorlar sonini kiriting : "))
col = int(input("Matritsa ustunlar sonini kiriting : "))

for x in range(row):
    ls = [randint(10,13) for x in range(col)]
    matrix.append(ls)

for x in matrix:
    for j in x:
        print("{}".format(j) , end = " ")
    print("")
    
r,c,max_num = None,None,0

for x in range(row):
    for j in range(col):
        if matrix[x][j] > max_num:
            max_num = matrix[x][j]
            r = x
            c = j
print(f"Eng katta qiymat = {max_num}; indexlari {r}:{c}")
