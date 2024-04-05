import os
os.system("clear")

# DONE

count = 0
k = None

while 1:
    number = int(input("Son = "))
    if k is not None and k > 0 and number > 0:
        count += 1
    elif k is None:
        k = number
    k = number
    if number == 0:
        break
if count >= 2:
    print("\n2ta qo'shni musbat son mavjud!")
else : 
    print("\n2ta qo'shni musbat son mavjud EMAS!")
