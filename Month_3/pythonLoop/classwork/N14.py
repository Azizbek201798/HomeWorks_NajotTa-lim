import os
os.system("clear")

num = int(input("5 xonali sonni kiriting = "))
sum = 0
while(num > 0):
    sum += num % 10
    num //= 10
print(f"Sum = {sum}")
