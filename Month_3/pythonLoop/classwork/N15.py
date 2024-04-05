import os
os.system("clear")

num = int(input("Ikki xonali sonni kiriting : "))
num = (num % 10) * 10 + num // 10
print("Reversed = ",num) 