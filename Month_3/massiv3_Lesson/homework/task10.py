# Topshiriq_10 => DONE by LeoMessi

# Dictionary ma'lumotlari berilgan va sizning vazifangiz ushbu dictionarydagi qiymati eng katta va eng kichik ma'lumotlarni o'chiring.
# Input: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# Output: {2: 20, 3: 30, 4: 40, 5: 50}

import os
os.system("clear")

dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
list1 = list(dict1.values())

print(f"Before : {dict1}")
x,k = 1,len(dict1)

while k > 0:
    if dict1[x] == min(list1) or dict1[x] == max(list1):
        dict1.pop(x) 
    k -= 1
    x += 1

print(f"After  : {dict1}")
