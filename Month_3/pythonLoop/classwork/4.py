print("Sonni kiriting :")
A = int(input())
for x in range(A + 1):
    if A % (x+1) == 0:
        print(x+1)