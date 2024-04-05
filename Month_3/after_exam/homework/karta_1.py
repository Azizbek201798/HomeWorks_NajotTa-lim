# Task - 3.1 => KARTA => SUCCESFULLY

# Karta_raqami,Karta_turi,Valyuta,Valyuta_kodi,Korxona,Davlat
# 1) Fayldagi davlatlarni nomlarini dictionary keysiga va qiymatiga esa ushbu davlatlar sonini yozib chiqaring;

import os
os.system("clear")
os.chdir("/home/azizbek/go/src/NajotTalim/HomeWork/Month_3/after_exam/homework")

f = open("karta.txt","r")
data = f.read()

data,dc = data.split("\n"),{}

for x in data:
    k = x.split(",")
    if k[-1] not in list(dc.keys()):
        dc[k[-1]] = 1
    else :
        dc[k[-1]] += 1

print(dc)