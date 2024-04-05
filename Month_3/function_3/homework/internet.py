# Task - 2 => INTERNET => SUCCESFULLY
 
# Faylda Email,File_name,Mac_adress,Level; 5F-A7-B9-CD-1A-F5 
# Ma'lumotlari berilgan 1) Mac adresida har bir ikkitalikda harf qatnashgan Email va File_name larni chiqaring 

import os
os.system("clear")
os.chdir("/home/azizbek/go/src/NajotTalim/HomeWork/Month_3/function_3/homework")

f = open("internet.txt","r")
data = f.read()

ls1,ls2,a = data.split("\n"),[],0
address = []

for x in ls1:
    k = x.split(",")
    r = k[2].split("-")
    check = True
    for z in r:
        if z.isdigit() or z.isalpha():
            check = False
            break
    if check == True:
        address.append(k[2])
        print(f"{a+1} - Email : {k[0]}; File_Name : {k[1]}")
        a += 1
     
print(f"\nMacAddresning har bir juftligi harfdan iborat bo'lgani JAMI {a} ta!")
for x in range(len(address)):
    print(address[x])