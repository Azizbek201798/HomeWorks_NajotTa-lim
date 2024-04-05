# Task - 3.2 => KARTA => SUCCESFULLY

# Karta_raqami,Karta_turi,Valyuta,Valyuta_kodi,Korxona,Davlat
# 2) Fayldagi karta turida visa qatnashgan davlatlarni alfavit tartibida chiqaring.

import os
os.system("clear")
os.chdir("/home/azizbek/go/src/NajotTalim/HomeWork/Month_3/after_exam/homework")

f = open("karta.txt","r")
data,st = f.read(),set()

for x in data.split("\n"):
    k = x.split(",")
    if k[1] == "visa":
        st.add(k[-1])

result = list(st)
result.sort()
print(result)
