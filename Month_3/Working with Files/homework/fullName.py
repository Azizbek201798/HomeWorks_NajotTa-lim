# Task - 1 => FULL_NAME => SUCCESFULLY

# Faylda ism va familiyalar berilgan. Ushbu fayldagi ma'lumotlarni familiyasi bo'yicha alfavit tartibida 
# saralaydigan va chiqarib beradigan method yarating. 

import os
os.system("clear")
os.chdir("/home/azizbek/go/src/NajotTalim/HomeWork/Month_3/function_3/homework")

# 1 - USUL 

try:
    ls=[]
    f = open("fullName.txt","r")
    data=f.read().split("\n")
    data.sort(key = lambda x: x.split()[1])
    for x in data:
        ls.append(x)
        print(x)

except:
    print("Faylni ochishda xatolik")

# 2 - USUL 

# f = open("fullName.txt","r")
# data = f.read()

# # Kiritilgan datani familiya bo'yicha sortlash
# def sortFamiliya(k : str):
#     k = k.split("\n")
#     ls = []

#     for x in k:
#         ls.append(x.split())

#     # Ism va Familiyanini o'rnini almashtirish
#     for x in range(len(ls)):
#         ls[x][0],ls[x][1] = ls[x][1],ls[x][0]

#     ls.sort()

#     # Familiya bo'yicha sortlashdan keyin Ism va Familiyanini o'rnini almashtirish
#     for x in range(len(ls)):
#         ls[x][0],ls[x][1] = ls[x][1],ls[x][0]
    
#     return ls 

# result = sortFamiliya(data)

# Familiya bo'yicha sortlashdan keyin chop etish
# for x in result:
#     print(f"{x[0]} {x[1]}")
