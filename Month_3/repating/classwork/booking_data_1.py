# 1. Foydalanuvchi o'zida bor taxminiy pul miqdorini kiritadi. Maqsadingiz shu kiritlgan summadan 
# $50 arzonroq va $100 qimmatroq bo'lgan biletlar ro'yhatini ko'rsatish

import os
os.system("clear")
os.chdir("/home/azizbek/go/src/NajotTalim/HomeWork/Month_3/repating/classwork")

f = open("booking_data.txt","r")
data = f.read().split("\n")

money = int(input("Kissayizda bor pulni kiriting dollarda : "))
count = 0

for x in data:
    k = x.split(",")
    if money > float(k[-1][1:]) - 50 and money < float(k[-1][1:]) + 100:
        print(f"{count + 1} - {k}")
        count += 1
