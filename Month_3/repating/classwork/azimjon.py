# Azimjon "Omad shou"ga chiqish uchun tinmasdan "Jesco" limonadlarini ichmoqda! Bugun u do'konga borib, 
# �
# n shisha limonad sotib oldi. Har bir shishada 
# �
# t litrdan limonat bor. U shishalarni bir qator qilib qo'ydi va quyidagilarni qila boshladi:
# 1. U bitta shisha oladi, undan 1 litr ichadi.
# 2. Ichgan shishasini qatorning oxiriga qo'yadi va keyingi shishaga o'tadi. Bu 2 ta harakat 1 ta qadam deb hisonlanadi.
# 
# �
# k ta qadamdan song Azimjon kamida bitta shishani bo'shata oladimi?

import os
os.system("clear")

n,t,k = map(int,input().split())

ls = []
for x in range(n):
    ls.append(t)

