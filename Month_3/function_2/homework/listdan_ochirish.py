# Massivdan o’chirish => Done by Azizbek

# N ta elementdan iborat massiv berilgan. Massiv qiymatlari [1, 100] oralig’idagi 
# qiymatlardan tashkil topgan. Massivning barcha elementi qiymati bir xil bo’lishi 
# uchun eng kamida nechta element o’chirilishi kerakligini aniqlang.

import os
os.system("clear")

def delNumber(N : int, x : list):
    dc = {}
    for x in ls:
        if x not in dc:
            dc[x] = 1
        else :
            dc[x] += 1
    print(N - max(list(dc.values())))

N = int(input())
ls = list(map(int,input().split()))

delNumber(N,ls)