# Topshiriq5***
# 1 dan n gacha bo'lgan sonlar ichidan tub sonlarni va ularning sonini ekranga chop qiladigan 
# algoritmni ishlab chiqing! Buning uchun ichma-ich siklni ixtiyoriy turidan foydalanishingiz mumkin.
# #takrorlanuvchi_python_topshiriq
import os
os.system("clear")

#DONE

n = int(input("n = "))
count = 0
for i in range(2,n+1):
    check = True
    for j in range(2,i-1,1):
        if (i) % (j) == 0:
            check = False
            break
    if check == True:
        count += 1
        print(i,sep = " | ")
print("{}ta tub son mavjud".format(count))
