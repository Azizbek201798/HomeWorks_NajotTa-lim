# T8 => DONE by Azizbek

# Function tuzing. Bu function natural sonlardan iborat list qabul qiladi. Va shu sonlardan yasash 
# mumkin bo'lsan eng katta qiymatni qaytaradi:
# Input:  [1, 2, 3]
# Output: 321
# Input:  [61, 228, 9]
# Output: 961228

import os
os.system("clear")

def max_num(ls: list):
    ls1,maxNum = [],""
    for k in range(len(ls)):
        max1 = str(ls[0])
        for a in ls:
            a = str(a)
            if len(a) > len(max1):
                k = len(max1)
            else:
                k = len(a)
                
            for x in range(k):
                if max1[x] < a[x]:
                    max1 = a
                    break
                if max1[x] == a[x] or max1[x] > a[x]:
                    continue
        ls1.append(max1)
        ls.remove(int(max1))
    for d in ls1:
         maxNum = maxNum + d
    return maxNum

listNew = list(map(int,input("sonlar: ").split())) 
print(int(max_num(listNew)))