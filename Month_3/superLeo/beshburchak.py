import os
os.system("clear")

def pentagonal(n):
    if n == 1:
        return 1
    else:
        return 5 * (n - 1) + pentagonal(n - 1)

n = int(input("N-iteratsiyani kiriting: "))
result = pentagonal(n)
print(result)