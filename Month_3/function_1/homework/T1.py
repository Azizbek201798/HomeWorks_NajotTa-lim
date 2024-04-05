# T1 => DONE by Azizbek

# Foydalanuvchi butun son kiritadi. Shu sonning raqamlari sonini aniqlovchi funksiya tuzing

import os
os.system("clear")

def digits(a : int):
    count = 0
    while a > 0:
        a //= 10
        count += 1
    print(f"Raqamlari soni = {count} ta")
    

number = int(input("Son kiriting : "))

digits(number)


