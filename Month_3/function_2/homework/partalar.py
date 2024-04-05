# Task 1 - Partalar : Done by Azizbek

# Karantindan so`ng bir maktabda yangi uchta matematikaga yo`naltirilgan sinf ochish va ular 
# uchun yangi partalar sotib olishga qaror qilindi. Har bir partada 2 kishi o`tirishi mumkin. 
# Uchta sinfda ham o`quvchilar soni aniq. Hammaga parta yetishi uchun eng kamida nechta parta 
# sotib olish kerak ekanligini aniqlang. Har bir sinf o`z xonasida o`tiradi. 

import os
os.system("clear")

sinf1,sinf2,sinf3 = map(int,input("O'quvchilar sonini kiriting : ").split())
count = 0

if sinf1 % 2 != 0:
    count += (sinf1 // 2) + 1
else :
    count += sinf1 // 2

if sinf2 % 2 != 0:
    count += (sinf2 // 2) + 1
else :
    count += sinf2 // 2

if sinf3 % 2 != 0:
    count += (sinf3 // 2) + 1
else :
    count += sinf3 // 2

print(count)








