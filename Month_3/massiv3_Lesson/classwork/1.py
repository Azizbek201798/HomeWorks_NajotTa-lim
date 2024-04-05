import random
import os
os.system("clear")

n = int(input("n = "))
mySet = set()

for x in range(n):
    mySet.add(random.randint(10,99))

print("Before : ",mySet)

a = map(int,input("Elementlarni kiriting : ").split())

for x in a:
    mySet.discard(x)

print("After : ",mySet)