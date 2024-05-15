import os
os.system("clear")

os.chdir("home/Azizbek/go/src")

# Azizbek 73
# Anvar.27

try:
    f = open("satr.txt")
    f.seek(0)
    data = f.read()
    summa = 0
    for x in data:
        num = ""
        if not x.isdigit():
            continue
        else :
            num += x
        summa += int(num)
    f.write(f"summa = {summa}")
    f.close()
    os.system("start home/Azizbek/go/src/satr.txt")
except:
    print("fayl topilmadi")