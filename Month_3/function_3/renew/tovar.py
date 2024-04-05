import os
os.system("clear")
os.chdir("/home/azizbek/go/src/NajotTalim/HomeWork/Month_3/function_3/renew")

try:
    f = open("tovarlar.txt","r")
    a = open("Aharfli.txt","w")
    k = open("Kharfli.txt","w")

    data = f.read().split("\n")

    for x in data:
        if 'a' in x or "A" in x:
            a.write(x + "\n")
        elif 'k' in x or "K" in x:
            k.write(x + "\n")

    f.close()
    a.close()
    k.close()

    print("Successfully wrote info to files!")
except:
    print("Faylni ochishda yoki o'qishda xatolik mavjud!")