# Task - 2 : Sezar shifrlash algoritmi => Done by Azizbek

# Maxfiy topshiriqlarni maktub orqali jo’natishda topshiriqning maxfiyligini ta’minlash maqsadida 
# Yuliy Sezar o’z maktublarida quyidagi shifrlash algoritmidan foydalanadi. Maktubda ishtirok etgan 
# katta va kichik lotin harflarining o’rniga alifboda shu belgidan K ta keyin kelgan harfni yozadi 
# (u alifboda z harfidan so’ng yana a harfi keladi deb hisoblaydi). Misol uchun K = 3 bo’lganida: 

# Xabar: abcdefghijklmnopqrstuvwxyz
# Shifr: defghijklmnopqrstuvwxyzabc

import os
os.system("clear")

k = int(input())
xabar = input()
shifr = ""

for x in xabar:
    if x.isalpha():
        if x.islower():
            base = ord('a')
        else :
            base = ord('A')
        letter = chr((ord(x) + k - base) % 26 + base)
        shifr += letter
    else :
        shifr += x

print(shifr)
