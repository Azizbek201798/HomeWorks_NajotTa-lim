# topshiriq5. A va B (A > B) musbat sonlar berilgan. 
# A kesmada B kesmani necha marta joylashtirish mumkin. 
# A kesmada B kesmaning jo yashmag an gismini aniqlovchi programma tuzilsin.

print("A va B ni qiymatini kiriting(A > B) : ")
print("A = ")
A = int(input())
print("B = ")
B = int(input())
print("B ni A kesmaga", A // B," marta joylashtirish mumkin va A kesmada B kesmaning joylashmagan qismi", A - (A // B) * B ,"ga teng!")