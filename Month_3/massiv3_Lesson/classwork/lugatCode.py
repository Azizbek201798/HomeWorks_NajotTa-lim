# X1:
# Lug'at dastur tuzasiz. Dastur run bo'lganda. 3ta menu chiqadi. 

# "1. So'z izlash 2. So'z qo'shish 3. So'z o'chirish 4.Chiqish".

# 1. 1ni tanlasa 2ta menyu chiqadi.
# 1. Uz - Eng 2. Eng - Uz

# 2. 2ni tanlasa 
# 1. Uz - Eng 2. Eng - Uz
# va so'z izlaydi.

# 3. ni tanlasa so'z so'raydi va shuni o'chirib tashlaydi.

# 4.ni tanlasa dastur tugaydi.

import os
import lugat
os.system("clear")

while True:
    print("1. So'z izlash\n2. So'z qo'shish\n3. So'z o'chirish\n4. Chiqish")
    n = int(input("\n1-4 gacha son tanlang : "))
    match n:
        case 1:
            print("1. Eng - Uz 2. Uz - Eng :",end = " ")
            k = int(input())
            match k:
                case 1:
                    word = input("So'z kiriting : ")
                    for x in range(len(lugat.dc)):
                        if lugat.dc[x]["english"] == word:
                            print(lugat.dc[x]["uzbek"])
                            print("")   
                case 2:
                    word = input("So'z kiriting : ")
                    for x in range(len(lugat.dc)):
                        if lugat.dc[x]["uzbek"] == word:
                            print(lugat.dc[x]["english"])
                            print("")
                case _:
                    print("Faqat 1 yoki 2 ni tanlang!")
        case 2:
            print("1. Eng - Uz 2. Uz - Eng :",end = " ")
            k = int(input())
            match k:
                case 1:
                    word1 = input("English : ")
                    word2 = input("Uzbek   : ")
                    lugat.dc.append({"english :": word1,"uzbek" : word2})             
                case 2:        
                    word1 = input("English : ")
                    word2 = input("Uzbek   : ")
                    lugat.dc.append({"english :": word1,"uzbek" : word2})             
        case 3: 
            word = input("So'z kiriting : ")
            for x in range(len(lugat.dc)):
                        if lugat.dc[x]["english"] == word:
                            lugat.dc.remove(word)  
                        elif lugat.dc[x]["uzbek"] == word:
                            lugat.dc.remove(word)
        case 4:
            break
        case _:
            print("Faqat 1 dan 4 gacha son kiriting!")

