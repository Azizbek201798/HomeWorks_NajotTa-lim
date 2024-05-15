import os
import random
os.system("clear")

ls = [random.randint(1,9) for x in range(10)]
print(ls)

res1 = list(map(lambda x : x * x,ls))
print(res1)

res2 = list(filter(lambda x : x % 2 == 0,ls))
print(res2)