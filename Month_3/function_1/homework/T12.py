# T12 => DONE by Azizbek

# Foydalanuvchi son kiritadi, sonning raqamlar yigindisi bir xonali bolib qolgancha hosil bolgan sonning raqamlar 
# yigindisini hisoblab yakuniy narijani qaytaruvchi function yozing.
# Input: 38
# Output: 2
# Tushuntirish: 38 => 3+8 => 11 => 1+1 = 2
# Input:96
# Output: 
# Tushuntirish: 96 => 9+6 => 15 => 1+ 5 => 6

import os
os.system("clear")

number = int(input("Son kiriting : "))

def sumDigit(z : int):
    sum = 0
    if z > 9:
        for x in str(z):
            sum += int(x)
        z = sum
    else :
        print(z)
        return  
    sumDigit(z)

sumDigit(number)