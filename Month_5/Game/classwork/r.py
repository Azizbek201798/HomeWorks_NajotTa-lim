import os
import random

os.system("clear")

ls = []
while len(ls) < 15:
    random_num = random.randint(1,15) 
    if random_num not in ls: 
        ls.append(random_num) 

print(ls)