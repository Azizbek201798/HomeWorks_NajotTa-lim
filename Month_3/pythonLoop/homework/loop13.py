import os
os.system("clear")

# DONE;

n = int(input("Ketma - ketlik sonini kiriting : "))
minPositive = None
maxNegative = None

for i in range(n):
    number = float(input("Son kiriting = "))
    if number > 0:
        if minPositive is None or number < minPositive:
            minPositive = number
    elif number < 0:
        if maxNegative is None or maxNegative < number:
            maxNegative = number

if minPositive is None:
    print("\nKetma-ketlikda musbat son mavjud EMAS!")
else :
    print(f"\n{minPositive} -> eng kichik musbat son")
    
if maxNegative is None:
    print("\nKetma-ketlikda manfiy son mavjud EMAS!")
else :
    print(f"\n{maxNegative} -> eng katta manfiy son")
