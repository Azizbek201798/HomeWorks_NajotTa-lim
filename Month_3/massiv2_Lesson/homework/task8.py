# Topshiriq_8
# MxN matritsani eng katta va eng kichik elementlarini almashtiring. Qiymatlarni
# tasodifiy sonlar generatori yordamida kiriting

import os
import random
os.system("clear")

M = int(input("M = "))
N = int(input("N = "))
massiv = []

# Fill list with random numbers: 
for x in range(M):
    massiv.append([random.randint(10,99) for y in range(N)])

max = massiv[0][0]
min = massiv[0][0]

print("\nBefore massiv : \n")
for x in range(M):
    for y in range(N):
        print("{:4d}".format(massiv[x][y]),end = "")
    print("\n")

# Find max and min
for x in range(M):
    for y in range(N):
        if massiv[x][y] >= max:
            max = massiv[x][y]
        elif massiv[x][y] < min:
            min = massiv[x][y]

# Change place
for x in range(M):
    for y in range(N):
        if massiv[x][y] == max:
            massiv[x][y] = min
        elif massiv[x][y] == min:
            massiv[x][y] = max

print("\nAfter massiv : \n")
# Show matrix elements
for x in range(M):
    for y in range(N):
        print("{:4d}".format(massiv[x][y]),end = "")
    print("\n")