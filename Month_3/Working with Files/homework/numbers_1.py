# Task - 4 => NUMBERS: => SUCCESFULLY

# Faylda telefon raqamlar berilgan.1) Ushbu fayldan barcha telefon raqam operatorlarini chiqaring. 

import os
os.system("clear")
os.chdir("/home/azizbek/go/src/NajotTalim/HomeWork/Month_3/function_3/homework")

f = open("numbers.txt","r")
data = f.read()

ls1,ls2 = data.split("\n"),[]

for x in ls1:
    ls2.append(x.split())

st = set()
for x in ls2:
    st.add(x[1])

print(f"Kompaniya Operatorlar : {st}")