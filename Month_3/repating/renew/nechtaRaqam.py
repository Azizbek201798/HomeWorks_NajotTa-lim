import os
os.system("clear")

text,count = input("Text kiriting : "),0

for x in text:
    if x.isdigit():
        count += 1

print(count)
