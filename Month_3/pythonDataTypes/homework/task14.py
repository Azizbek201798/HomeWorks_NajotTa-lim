# topshiriq14. Uch xonal son berilgan.
# Uning ongdan birinchi ragamini o'chirb chap tarafiga yozishdan ho sil bo Igan sonni aniqlovchi programma tuzilsin.

print("Uch xonali son kiriting : ")
A = int(input())
newNumber = A % 10 * 100 + ((A // 10) // 10) * 10 + A // 10 % 10
print("NewNumber = ", newNumber)