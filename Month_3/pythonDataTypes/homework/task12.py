# topshiriq12. Uch xonali son berilgan.
#  Uning raqamlarini teskari tartibda yozishdan hosil bo Igan sonni aniqlovchi program tuzilsin.

print("Uch xonali son kiriting : ")
A = int(input())
rev = (A % 10) * 100 + ((A // 10) % 10) * 10 + (A // 10) // 10
print("Reversed = ",rev)