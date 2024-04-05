# topshiriq16. Uch xonali son berilgan. 
# Uning o'nliklar xonasidagi raqam bilan birliklar xo na sidagi raqamni
# almashtirishdan ho sil bolgan sonni aniglovchi programma tuzilsin. (Kirish =123; Natija = 132)

print("Uch xonali son kiriting : ")
A = int(input())
newNumber = A // 10 // 10 * 100 + A % 10 * 10 + A // 10 % 10
print("NewNumber = ",newNumber)