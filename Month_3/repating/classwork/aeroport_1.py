import os
os.system("clear")
os.chdir("/home/azizbek/go/src/NajotTalim/HomeWork/Month_3/repating/classwork")

f = open("aeroport.txt","r")
data = f.read().split("\n")
dc,count = {},0

for x in data:
    k = x.split(",")
    if k[2] not in list(dc.keys()):
        dc[k[2]] = 1
        count += 1
    else :
        dc[k[2]] += 1

print(dc)
print(f"Xillari : {count}")