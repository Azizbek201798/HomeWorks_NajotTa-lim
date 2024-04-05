import os
os.system("clear")

from itertools import combinations

def find_banknotes(S, banknotes):
    N = len(banknotes)
    for i in range(1, N + 1):
        for comb in combinations(banknotes, i):
            total = sum(comb)
            if total == S:
                return comb
    return None

# Input
S = int(input("S = "))
N = int(input("N = "))
banknotes = list(map(int, input("P1,P2,P3... = ").split()))
M = int(input("M = "))
payment_banknotes = list(map(int, input("Q1,Q2,Q3... = ").split()))

# Find valid combination
valid_combination = find_banknotes(S, banknotes)

# Output
if valid_combination is None:
    print("Impossible")
else:
    for note in banknotes:
        if note in valid_combination:
            print("+" + str(note), end=" ")
        else:
            print("-", end=" ")