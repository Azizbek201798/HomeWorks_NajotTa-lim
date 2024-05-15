# Task - 4.2 => NUMBERS: => SUCCESFULLY

# Faylda telefon raqamlar berilgan. 2) Ushbu fayldagi 7ta takrorlanmagan raqamli telefon raqamini chiqaring.

# 1 - USUL

import os
os.system("clear")
os.chdir("/home/azizbek/go/src/NajotTalim/HomeWork/Month_3/function_3/homework")

f = open("numbers.txt","r")

data = f.read()
ls1 = data.split("\n")
print(f"Barcha raqamlar : \n{ls1}\n")
print(f"Ohirgi 7 Raqamlari takrorlanmaganlari : ")
for x in ls1:
    st = set()
    for y in x[8:]:
        if y.isdigit():
            st.add(y)
    if len(st) == len(x[8:]) - 2:
        print(x)

# 2 - USUL
        
# import os
# os.system("clear")
# os.chdir("/home/azizbek/go/src/NajotTalim/HomeWork/Month_3/function_3/homework")

# f = open("numbers.txt","r")
# data = f.read()

# ls1, raqam, uniqueDigitNumbers,count = data.split("\n"),[],[],0

# # 7 talik telefon raqamlarni datadan olish
# for x in ls1:
#     raqam.append(x[8:11] + x[12:14] + x[15:17])

# for r in raqam:
#     st = set()
#     for y in r:
#         st.add(y)
#     if len(st) == len(r):
#         count += 1
#         uniqueDigitNumbers.append(r)

# print(f"Barcha raqamlar : {raqam}")
# print(f"\nRaqami takrorlanmaganlari : {uniqueDigitNumbers}")
# print(f"\nJAMI : 50ta raqamdan {count} ta sining ohirgi 7 ta raqami takrorlanmagan!")