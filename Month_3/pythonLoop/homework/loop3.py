import os
os.system("clear")

# DONE

n = int(input("n = "))
count, mult, maxNum = 0,1,0
while n > 0:
    num = int(input("{} - son = ").format(count + 1))
    if num < 0:
        maxNum = num
    if num % 2 != 0:
        mult *= num
    if num < 0 and maxNum < num:
        maxNum = num 
    n -= 1
if maxNum == 0:
    print("Toq sonlar ko'paytmasi = {}, Manfiy son kiritilmadi!".format(mult))
else :
    print("Toq sonlar ko'paytmasi = {}, Max = {}".format(mult,maxNum))
