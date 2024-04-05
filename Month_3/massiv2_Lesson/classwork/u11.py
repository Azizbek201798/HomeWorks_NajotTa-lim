import os
os.system("clear")

ls = [1,0,9]

a = str(ls)
a = a[1:-1]
a = a.replace(",", "").replace(" ", "")
print(a)
b = list(map(int, list(str(int(a) + 1))))
print(b)
