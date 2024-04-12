import os
os.system("clear")

# CodeWars Degree 7

n,m = map(int,input("n,m = ").split())

def cook_pancakes(n, m):
    time = n // m * 2 + n % m * 2
    return time

print(cook_pancakes(n,m))