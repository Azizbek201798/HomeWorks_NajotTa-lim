import os
os.system("clear")

number = int(input("7 xonali sonni kiriting : "))
son = number
number = 0
while (son > 0):
    number = number * 10 + son%10
    son //= 10
print(f"Result = {number}")