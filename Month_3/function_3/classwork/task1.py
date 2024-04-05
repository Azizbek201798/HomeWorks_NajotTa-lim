import os
os.system("clear")

os.chdir("/home/azizbek/go/src")

try:
    fayl = open("task1.txt","wt")
    fayl.write("""Lorem 
               Ipsumha 
               unknown 
               It hass 
               remainin
               Letraset 
               PageMake
               """)
except:
    print("Error while writing file")

print("Completed")

fayl.close()

try:
    fayl = open("task1.txt")
    data = fayl.readlines()
    for x in data:
        if len(x) % 2 == 0:
            print(x)
except:
    print("Error while writing file")
