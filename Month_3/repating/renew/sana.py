import os
os.system("clear")

sana = input("Sanani kiriting : ")
oylar = ["January", "February", "March", "April", "May","June", "July", "August", "September", "October", "November", "December"]

ls = sana.split()
oy = int(ls[0].split(".")[1])
kun = int(ls[0].split(".")[0])
yil = int(ls[0].split(".")[2])

soat = int(ls[1].split(":")[0])
minut = int(ls[1].split(":")[1])

print(f"{kun} {oylar[oy-1]} {yil} year {soat} hours {minut} minutes ")
