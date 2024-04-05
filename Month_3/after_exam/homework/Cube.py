import os
os.system("clear")

def kubmi(n):
    return n ** (1/3) == int(n ** (1/3))

t = int(input())
for _ in range(t):
    n = int(input())
    if kubmi(2*n + 3*n + 5*n + 6*n):
        print("YES")
    else:
        print("NO")
    
# ACCEPTED 100%