# Task - 3.3 => KARTA => SUCCESFULLY

# Karta_raqami,Karta_turi,Valyuta,Valyuta_kodi,Korxona,Davlat
# 3) Karta raqami orasida kamida hamma raqamlar,ya'ni 0,1,2,3,4,5,6,7,8,9 
# ishtirok etganlarni karta_raqami,davlat,valyuta va korxonasini chiqarib bering

import os
os.system("clear")
os.chdir("/home/azizbek/go/src/NajotTalim/HomeWork/Month_3/function_3/homework")

f = open("karta.txt","r")
data = f.read()

count = 0
for x in data.split("\n"):
    k = x.split(",")
    st = set()
    for z in k[1]:
        st.add(z)
    if len(st) == 10:
        count += 1
        print(f"Karta raqami : {k[0]} Davlati : {k[-1]} Valyuta : {k[2]} Kompaniya : {k[-2]}")

print(f"\nJAMI : 1000 ta davlatdan {count} tasi shartlarga mos keldi!")