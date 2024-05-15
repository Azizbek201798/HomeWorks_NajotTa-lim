# R3: 
# Ushbu faylda nechta so'z borligini aniqlang.

import os
os.system("clear")
os.chdir("/home/azizbek/go/src/NajotTalim/HomeWork/Month_3/function_3/classwork")

f = open("soz.txt","r")
data = f.read()

data = data.split()
data = list(map(lambda x : x.replace(".","").replace(",",""), data))

for x in range(len(data)):
    data[x].replace(".","")

dc = {}

for x in data:
    if x not in dc:
        dc[x] = 0
    else :
        dc[x] += 1
print(dc)
print(max(list(dc.values())))