import os
os.system("clear")

#DONE

n = int(input("Yulduzchalar sonini kiriting = "))
for i in range(n):
    for j in range(n - i):
        print("*",end = " ")
    print("\n")