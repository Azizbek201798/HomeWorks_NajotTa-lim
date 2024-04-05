# Topshiriq_9 => DONE by LeoMessi

# N soni input orqali kiritiladi va dictionary kalitiga 1dan Ngacha sonlarni va qiymatlariga ushbu kalitlarning kvadratlarini yozing.
# Input: N=6
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

import os
os.system("clear")

N = int(input("N = "))
dict1 = {}

k = 1
while N > 0:
    dict1.update({k : k * k})
    k += 1
    N -= 1

print(dict1)

