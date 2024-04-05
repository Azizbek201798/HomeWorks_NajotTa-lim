import os
os.system("clear")
os.chdir("/home/azizbek/go/src/NajotTalim/HomeWork/Month_3/repating/classwork")

f = open("aeroport.txt","r")
data = f.read().split("\n")
data.sort(key = lambda x : x.split(",")[-1][1:])

print(f"Min : {data[0][4:]}")
print(f"Max : {data[-1][4:]}")


