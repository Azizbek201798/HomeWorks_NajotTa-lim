import os
os.system("clear")
os.chdir("/home/azizbek/go/src/NajotTalim/HomeWork/Month_3/repating/classwork")

f = open("car.txt","r")
ls = []
data = f.read().split("\n")
data.sort(key = lambda x : x.split(",")[2])
for x in data:    
    ls.append(x)
    print(x)