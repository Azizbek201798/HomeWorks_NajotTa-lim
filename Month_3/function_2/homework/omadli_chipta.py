# Omadli chipta => DONE by Azizbek

# Otabek Jamoat transporti uchun chipta sotib olish uchun shaxobchaga boribdi.
# Transport agentligi tamonidan chegirmali chipta elon qilingan ekan, 
# Chegirma Omadli chipta egasiga berilar ekan. Omadli chipta bo’lishi uchun 
# chiptaning raqami 6 xonali bo’lishi va birinchi 3 ta raqamining yigindisi 
# oxirgi 3 ta raqamining yig’indisiga teng bo’lishi kerak. 
# Sizning vazifangiz Omadli Chiptani aniqlash dasturini tuzish.

import os
os.system("clear")

def omadliChipta(num : int):
    num = str(num)
    if len(num) == 6 and (int(num[0]) + int(num[1]) + int(num[2]) == int(num[3]) + int(num[4]) + int(num[5])):
        print("YES")
    else :
        print("NO")

N = int(input())
omadliChipta(N)

