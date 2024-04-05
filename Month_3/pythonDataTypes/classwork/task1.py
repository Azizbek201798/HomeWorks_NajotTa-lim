import os

os.system("clear")

''' 1) a = 77
print(a)'''

''' 2) s = "Salom python"
print(s) '''

''' 3) a = 105
a = 'Bugun bayram emas' 
print(a) '''

''' 4) a = "toilet"
print(type(a)) '''

''' 5)b = 127
print(type(b)) '''

''' 6) a = 27
       b = 10
print(a/b)  -> kasr qismga bo'lish''' 

''' 7) a = 2
print(a ** 10)    -> darajaga oshirish
print(a ** (1/2)) -> darajaga oshirish
print(a % 10)     -> sonni qoldig'ini olish '''

''' 8) a = 100 -> bunda 100 ni 2 ning 4 darajasiga bo'lib butun qismini qaytaradi;
    a >>= 4 is equal with a = >> 4; 
print(a)
Result = 6 '''

''' 9) a = 100 -> bunda 100 ni 2 ning 4 darajasiga ko'paytirib butun qismini qaytaradi;
    a <<= 4 is equal with a = << 4; 
print(a)
Result = 1600 '''

''' 10) a = 366
        a = a % 2 == 0
    print(a)
    print(type(a))
    Result : True 
             <class 'bool'> '''

''' 11) a = "Maktab"
        b = 'maktab'
print(a >= b)
Result : False '''

''' 12) a = "Hamyon"
        b = 'Hamyon'
        x = 321
        y = 123
        print(a == b)
        print(x != y)
        Result : True
        Result : True '''

''' 13) z = 1
        a = 2
    z = bool(z)
    a = float(a)
    print(type(z))
    print(a)
    Result = <class 'bool'> 
    Result = 2.0 
    && -> and
    || -> or '''  

''' 14) f = 3.145678
    print(type(f))    
    result : <class 'float'> '''

''' 15) a = "Salom bevafo dunyo"
print(len(a)) -> berilgan satr uzunligini hisoblash;
Result : 18 '''

# a = "Barselona albatta yutadi"
# print(a.split()[0]) // Satrdagi 1-belgini oladi a.split() default holatda probel bo'yicha so'zni bo'ladi; 
# print(a[0:9]) ;Result : Barselona
# print(a[:17]) ;Result : Barselona albatta
# print(a[18:]) ;Result : yutadi
# print(a[0:24:2]); Result : Breoaabtaytd;
# print(a[0::3]) Result : Bso btya
# Result : 'Barselona'

# a = "Azizbek"
# print(a[::-1]) # Result : "kebzizA" -> berilga strni reverse qilib beradi;

# a = "AzIzBeK"
# print(a.lower()) # Result : "azizbek"
# print(a.upper()) # Result : "AZIZBEK"
# print(a.swapcase()) # Result : "aZiZbEk"

# a = "Agent007"
# print(a.isdigit()) # Result : False chunki variabledagi barcha element son emas
# print(a.isalpha()) # Result : False chunki variabledagi barcha element harf emas

# r = "My name is {}"
# name = "Azizbek"
# print(r.format(name))

# k = "My name is {}, surname is {}"
# name = "Azizbek"
# surname = "Ziyodullayev"
# print(k.format(name,surname))

# a = "My name is {1}, surname is {0}"
# name = "Azizbek"
# surname = "Ziyodullayev"
# print(a.format(name,surname))

# T_Min = -5
# T_Max = 15
# degree = "Degree of tomorrow from {:+} to {:+}"
# print(degree.format(T_Min,T_Max))
# Result : Degree of tomorrow from {-5} to {+15}

# s = "#" * 10
# print(s) # Result ##########

# a = "A"
# print(ord(a)) # Result : 65;

# print(sep = " ", end = "\n"); Print ni o'zini shunday xususiyati bor;
# a = "Azizbek"
# b = 'Kamola'
# print(a,b) # Result : "Azizbek Kamola"

# day = 27
# month = 5
# year = 1998
# print(day,month,year,sep = ".") # Result : 27.5.1998

# day = 2
# month = 5
# year = 1998
# print("{:02d}/{:02d}/{:04d}".format(day,month,year)) # Result : 02/05/1998
# bu yerda d -> digital butun son o'rnida ishlatilayapdi;

# a = 7
# b = 18
# c = 75
# print("O'nlikda {0} ; Ikkilikda       {0:b}".format(a,a)) #Result : 111 -> ikkilikda 
# print("O'nlikda {0} ; Sakkizlikda     {0:o}".format(b,b)) #Result : 22  -> 8 likda 
# print("O'nlikda {0} ; O'n Oltilikda   {0:X}".format(c,c)) #Result : 4B  -> 16 likda 

# son = 65
# print("Belgi {:c}".format(son)) # Result : Belgi A

# Task - 1
# a,b,c = map(int,input("Uchta sonni kiriting : ").split())
# Min, Max = min(a,b,c),max(a,b,c)
# Middle = a+b+c - Min - Max
# print(f"Min = {Min}\nMax = {Max}\nMiddles = {Middle}")

# print(int(input("Sonni kiriting : ")) ** 3); Result = 125











