import os 
os.system("clear")

number = int(input("Sonni kiriting : "))
for x in range(number + 1):
    if number % (x+1) == 0:
        print(f"{x+1}",end = "->")
 