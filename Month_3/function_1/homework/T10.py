# T10 => DONE by Azizbek

# Foydalanuvchi listga istalgancha qiymat kiritadi, siz shu qiymatlar ichidan faqat bir marta takrorlangan raqamlar sonini 
# qaytaruvchi funksiya tuzing, unday sonlar yoq bolsa -1 qaytarsin.
# Input:[4,1,2,1,2]
# Output: 1
# Input:[1,2,3,1,1]
# Output: 2

import os
os.system("clear")

ls1 = list(map(int,input("List elementlarini kiriting : ").split()))

def countUnique(z : list):
    dc1,count = {},0
    for x in z:
        if x not in dc1.keys():
            dc1[x] = 1
        else :
            dc1[x] += 1
    
    for y in dc1.values():
        if y == 1:
            count += 1
    os.system("clear")
    print(f"List : {ls1}")
        
    if count != 0:
        return count
    else :
        return -1
            
res = countUnique(ls1)
print(f"Bir marta takrorlangan elementlar soni : {res}")