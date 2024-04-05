import os 
os.system("clear")

Number = int(input("Sonni kiriting : "))
count = 0
while Number > 0 :
    print(f"{Number % 10}",end = "->")
    Number //= 10
    count += 1
print(f"\n{count} ta raqam mavjud")
