import os
os.system("clear")

dc = {0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}
N,count = int(input()),0
N = str(N)

for x in range(len(N)):
    if int(N[x]) in list(dc.keys()):
        count += dc[int(N[x])]

print(count)