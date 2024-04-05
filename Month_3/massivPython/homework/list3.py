# Topshiriq_3***
# Listni Nta sonlar bilan input orqali kiriting. Ushbu sonlardan faqat 2marta 
# va undan ko'p takrorlanganlarni faqat 1tasini qoldiring va saralang.
# Input: N=8 sonlar=[1,2,6,4,3,2,4,6]
# Output: sonlar=[1,2,3,4,6]
import os
os.system("clear")

N = int(input("Elementlar sonini kiriting : "))
massiv = []

for x in range(1,N+1):
    num = int(input("num = "))
    massiv.append(num)

newMassiv = list()
check = True

# Check list and append
for y in massiv:
    if y not in newMassiv:
        newMassiv.append(y)
print(newMassiv)
