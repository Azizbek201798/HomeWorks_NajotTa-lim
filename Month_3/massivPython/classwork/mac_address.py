import os
os.system("clear")

password = input("Satr kiriting : ")
arr = password.split("-")
check = True

for x in arr:
    if  x.isalpha() or x.isdigit():
        check = False
        break
print(check)