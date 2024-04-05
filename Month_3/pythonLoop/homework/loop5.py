import os
os.system("clear")

#DONE

n = int(input("Elementlar sonni kiriting : "))
maxNumber = None

while n > 0:
    number = int(input("Son = "))
    if maxNumber is None and number % 11 == 0:
        maxNumber = number
    if number % 11 == 0 and maxNumber < number:
        maxNumber = number
    n -= 1

if maxNumber != None:
    print(f"MaxNumber = {maxNumber}")
else :
    print("11 ga karrali son mavjud emas")
