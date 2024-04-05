import os
os.system("clear")
os.chdir("/home/azizbek/go/src/NajotTalim/HomeWork/Month_3/repating/classwork")

f = open("car.txt","r")
data = f.read()
dc = {}

for x in data.split("\n"):
    k = x.split(",")
    if k[-1] not in list(dc.keys()):
        dc[k[-1]] = 1
    else :
        dc[k[-1]] += 1

print(dc)