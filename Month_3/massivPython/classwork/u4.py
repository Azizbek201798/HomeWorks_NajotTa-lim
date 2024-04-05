# Belgilangan List raqamlarini undan juft raqamlarni olib tashlagandan 
# so'ng chop etish uchun Python dasturini yozing. 

# Namuna roʻyxati :  lst = [23, 44, 56, 99, 111, 23, 54]
# Kutilayotgan natija: [23, 99, 111, 23]
import os 
os.system("clear")

ls = list((12,12,12,4,66,45,79,22,12,66,66,66,53,2,9))
count = 0

for x in range(len(ls)):
    if ls[x] % 2 == 0:
        ls[x] = 0
        count += 1

for k in range(count):
    ls.remove(0)
print(ls)
