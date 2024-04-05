import os
os.system("clear")

massiv,count = list(map(int,input("Elementlarni kiriting : ").split())),0

while True:
    check = True
    for x in massiv:
        count += 1
        if x % 2 == 1:
            massiv.remove(x)
            check = False
            break
    if check == True:
        break
print(massiv)
print(f"Aylandi {count} marta")
