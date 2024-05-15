import os
os.system("clear")

k = open("satr.txt","at+")
k.seek(0)
data = k.read()
sum = 0
for x in data:
    if x.isdigit():
        sum += int(x)
k.write(f"\nSumma = {sum}")
k.close()