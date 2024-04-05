# DICTIONARY FUNKSIYALARI

# Dictionary(lug’at) – bu kalit,qiymat juftligi hisoblanadi. Dictionary kalitlar bo’yicha unikal bo’ladi.
# Dictionryni e’lon qilish usullari: 
# 1) lugat = {}
# 2) dict – classidan obyekt olish orqali; M-n : fr = dict()

# 1) update(item) → dict ga agar kiritilayotgan key yo’q bo’lsa o’sha key va value ni qo’shib qo’yadi. Agar kiritilayotgan key mavjud bo’lsa valuesini o’zgartiradi.
# 2)  items() → dictdagi qiymat va kalitlarni listni ichiga tuple ko’rinishida joylashtiradi.
# M-n: mine = {75 : "Termiz",10:"Toshkent"}
# massiv = mine.items()
# print(massiv)
# Result : dict_items([(75, 'Termiz'), (10, 'Toshkent')])
# 3) keys() → dict dagi barcha keylarni qaytaradi
# M-n: mine = {75 : "Termiz",10:"Toshkent"}
# print(mine.keys())
# Result : dict_keys([75, 10])
# 4) pop(key) → dict dan kiritilgan key bo’yicha elementni o’chiradi. 
# 5) popitem() → dictdagi ohirgi turgan elementni o’chirib beradi va o’chirgan elementni tuple ko’rinishida qaytaradi.
# 6) values() → dict dagi barcha valuelarni qaytaradi
# mine = {75 : "Termiz",10:"Toshkent"}
# print(mine.values())
# Result : dict_values([‘Termiz’, ‘Tashkent’])
# 7) setdefault() → berilgan juftlikni dictga qo’shadi. Agar juftlikda kalitning o’zi berilsa, value qismiga None ni yuklaydi. Agar juftlik mavjud bo’lsa oldingi qiymatni o’zgartirmaydi.
# 8)  fromkeys(ls) → massiv elementlarini dict ning keylariga qo’yib beradi,valuelariga esa None ni qo’yib beradi.
# M-n:
# my = dict()
# massiv = {1,2,3,4,5,6}
# my = my.fromkeys(massiv)
# print(my)
# 9) get(item_key) → dictdan key bo’yicha valueni olib beradi;
# M-n: x[7] va x.get(7) ning farqi getda agar yo’q keynit olishni aytsak xatolik bermaydi, 1-holda xatolik beradi.

# LAMBDA fuction 

# n = int(input("n = "))
# 
# def kopaytma(n : int):
#   return lambda a : a * n
# 
# result = kopaytma(2)
# 
# print(f"Result = {result(n)}")

# Bu kopaytma funksiya bizga anonim ya'ni nomsiz lambda funksiyasini qaytaradi shuning uchun uni result degan qiymatga o'zlashtirdim
# va uni resultga ohirida qiymat berib chaqirdim

