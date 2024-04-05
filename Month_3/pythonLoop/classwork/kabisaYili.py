import os 
os.system("clear")

year = int(input("Yilni kiriting = "))
if year % 400 == 0:
    print(f"{year} - yil Kabisa yili")
elif year % 100 == 0:
    print(f"{year} - yil Kabisa yili EMAS")
elif year % 4 == 0:
    print(f"{year} - yil Kabisa yili")
else :
    print(f"{year} - yil Kabisa yili EMAS")
    