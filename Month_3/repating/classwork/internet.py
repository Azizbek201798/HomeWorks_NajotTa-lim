import os
os.system("clear")
os.chdir("/home/azizbek/go/src/NajotTalim/HomeWork/Month_3/repating/classwork")

f = open("internet.txt")
data = f.read().split("\n")
dc,count = {},0
for x in data:
    k = x.split(",")
    z = k[0].split(".")
    if z[-1] not in list(dc.keys()):
        dc[z[-1]] = 1
        count += 1
    else :
        dc[z[-1]] += 1

print(dc)
print(f"Jami : {count} ta xil davlat")