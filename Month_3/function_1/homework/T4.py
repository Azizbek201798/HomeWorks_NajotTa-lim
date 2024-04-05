# T4 => DONE by Azizbek

# Shunday function tuzingi, bu function to'g'ri to'rtburchakning eni va bo'yini qabul qiladi. Function to'g'ri to'rtburchakning 
# perimetri va yuzasini tuple ko'rinishida qaytaradi
# Input:
# 5, 6
# Output:
# (22, 30)

import os
os.system("clear")

a,b = map(int,input("a,b = ").split())
st1 = []

def tortburchak(x : int, y : int):
    st1.append(2*(x+y))
    st1.append(x*y)

tortburchak(a,b)
print(f"Result(Perimetr,Yuza) = {tuple(st1)}")

