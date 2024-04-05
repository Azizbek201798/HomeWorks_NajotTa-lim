import os
os.system("clear")
os.chdir("/home/azizbek/go/src/NajotTalim/HomeWork/Month_3/repating/classwork")

f1 = open("raqamlar.txt","r")
f2 = open("tartibli.txt","w")

data = f1.read().split("+")


for x in data:
    f2.write(x + "\n")

f1.close()
f2.close()