import os
os.system("clear")

#DONE

N = int(input("Elementlar sonini kiriting : "))
count  = 0
sumNew = 0
while N > 0:
    number = float(input("HaqiqiySon = "))
    if number % 7 == 0:
        sumNew += number
        count += 1
    N -=1
avg = sumNew / count
print(f"7 ga karrali sonlar yig'indisi = {avg}")
