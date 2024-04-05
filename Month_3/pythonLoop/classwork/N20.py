import os
os.system("clear")

soz = input("Satrni kiriting : ")
soz[0], soz[len(soz) - 1] = soz[len(soz) - 1], soz[0]
print(soz)