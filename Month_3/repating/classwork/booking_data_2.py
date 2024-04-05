# 2. Kiritilgan davlat bo'yicha barcha aviareyslarni toping. Lekin chiqishda faqat soat 12:00dan 21:00gacha bo'lgan reyslar chiqsin.

import os
os.system("clear")
os.chdir("/home/azizbek/go/src/NajotTalim/HomeWork/Month_3/repating/classwork")

f = open("booking_data.txt","r")
data = f.read().split("\n")

country = input("Davlat nomini kiriting : ")
dc = {}

for x in data:
    k = x.split(",")
    ls = k[2].split(":")
    soat = int(ls[0])
    minut = int(ls[1])
    if k[1] not in list(dc.keys()) and (soat >= 12 and minut >= 0 and minut <= 59) and (soat <= 21 and minut <= 0) :
        dc[k[1]] = ""
    else:
        dc[k[1]] += str(soat + " : " + minut + ", ")

print(dc)