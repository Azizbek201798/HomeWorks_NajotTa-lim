import os
os.system("clear")

#DONE

count = 0
sumNegatives = 0
while 1:
    number = int(input("Sonni kiriting : "))
    if number % 7 != 0 and number % 5 != 0:
        count += 1 
    if number < 0 :
        sumNegatives += number
    if number == 0:
        break
print(f"\n5ga va 7 ga karrali bo'lmagan elementlar soni = {count} ta;\nManfiy sonlar yig'indisi = {sumNegatives}")