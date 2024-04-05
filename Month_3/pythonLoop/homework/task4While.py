# Topshiriq4
# while yordamida kompyuter o'ylagan sonni nechta urinishda topish mumkinligini hisoblab beruvchi algoritmni hosil qiling! 
# P/S: Ushbu holatda x soni berilgan deb hisoblansin. Ushbu qiymat foydalanuvchi tomonidan kiritilayotgan y ga teng bo'lishi kerak

import os
os.system("clear")

# DONE

x = 100
count = 0
while 1 :
    num = int(input("{} - Sonni kiriting : ".format(count + 1)))
    if num < x:
        print("Tepaga")
    else :
        print("Pastga")
    count += 1 
    if x == num :
        print("\n{} ta urinishda topdiz!".format(count))
        break

