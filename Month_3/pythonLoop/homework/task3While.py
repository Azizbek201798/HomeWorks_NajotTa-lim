# ***Topshiriq3***
# while yordamida ikkita butun son uchun EKUB(a,b) ni topuvchi algoritmni yarating. 
# P/S: EKUB-Eng katta umumiy bo'luvchi. M: EKUB(12,18)=6 ya'ni 12 va 18 ning eng katta bo'linadigan qiymati bu 6!
import os
os.system("clear")

# DONE

a = int(input("a = "))
b = int(input("b = "))
min = a
EKUB = 1 
if min > b:
    min = b
while min > 0:
    if a % min == 0 and b % min == 0:
        EKUB = min
        break
    min -= 1
print("Ekub({},{}) = {}".format(a,b,EKUB))
