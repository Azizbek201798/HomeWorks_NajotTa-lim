# topshiriq15. Uch xonali son berilgan.
#  Uning o nliklar xonasidagi raqam bilan yuzliklar xonasidagi raqamni
# almashtirishdan ho sil bo Igan sonni aniqlovchi programma tuzilsin. (Kirish =123; Natija = 213)

print("Uch xonali son kiriting : ")
A = int(input())
newNumber = A // 10 % 10 * 100 + A // 10 // 10 * 10 + A % 10 
print("NewNumber = ",newNumber)