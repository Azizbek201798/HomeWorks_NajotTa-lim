# Robo Password
# Robocontest.uz tizimiga ro'yhatdan o'tish uchun sayt adminlari tomonidan qo'yilgan talablarni bajarishingizga to'g'ri keladi. 
# Qoidalarga ko'ra saytda sizning parolingiz quyidagicha bo'lishi kerak.

# 1. Parol 9 xonali son bo'lishi kerak (0 bilan boshlanmagan).
# 2. Paroldagi raqamlar yig'indisi albatta toq son bo'lishi kerak.

# Agar yuqoridagi qoidalarga ko'ra parol tanlasangiz sizda muammo bo'lmaydi!!! 

import os
os.system("clear")

parol,summa = input(),0
for x in parol:
    summa += int(x)

if len(parol) == 9 and not parol.startswith("0") and summa % 2:
    print("yes")
else :
    print("no")
