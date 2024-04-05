import os
os.system("clear")

massiv = [12,34,98,34,7,17,76,7,87]
print(massiv)
find = int(input("Qidirilayorgan elementni kiriting : "))
check = True

for x in range(len(massiv)-1,-1,-1):
    if find == massiv[x]:
        check = False
        break
if check == True:
    print("NOT FOUND!")
else : 
    print("Index = ",x)