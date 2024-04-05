import os
os.system("clear")

month = int(input("Enter a month number (1-12): "))

if month in [1, 2, 12]:
    print("Winter")
elif month in [3, 4, 5]:
    print("Spring")
elif month in [6, 7, 8]:
    print("Summer")
elif month in [9, 10, 11]:
    print("Autumn")
else:
    print("Invalid month number")