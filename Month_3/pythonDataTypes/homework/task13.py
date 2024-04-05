# topshiriq13. Uch xonal son berilgan.
#  Uning chapdan birinchi raqamini o'chirib oing tarafiga yozishdan ho sil bo Igan sorini aniqlovchi programma tuzilsin.

print("Uch xonali son kiriting : ")
A = int(input())
newNum = ((A // 10) % 10) * 100 + (A % 10) * 10 + (A // 10) // 10
print("NewNumber = ",newNum)