# topshiriq11. Uch xonali son berilgan.
#  Uning raqamlar yig indisini aniqlovchi programma tuzilsin.

print("Uch xonali son kiriting : ")
A = int(input())
sum = (A // 10) // 10 + (A // 10) % 10 + A % 10
print("Raqamlari yig'indisi ",sum)