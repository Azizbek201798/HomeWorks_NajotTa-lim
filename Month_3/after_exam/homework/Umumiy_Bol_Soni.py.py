import os
os.system("clear")

n, m = map(int, input().split())
while m:
    n, m = m, n % m
gcd_value = n
count = sum(2 for i in range(1, int(gcd_value ** 0.5) + 1) if gcd_value % i == 0) - (gcd_value ** 0.5 == int(gcd_value ** 0.5))
print(count)

# 199 ta Case dan O'tdi 200-case da TimeLimit berdi!