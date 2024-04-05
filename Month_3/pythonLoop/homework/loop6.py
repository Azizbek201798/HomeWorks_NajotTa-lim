import os
os.system("clear")

#DONE

count = 0

while 1:
    number = int(input("Sonni kiriting : "))
    if number % 2 == 0 and number < 0:
        count += 1 
    if number == 0 :
        break
if count >= 3:
    print(True)
else :
    print(False)