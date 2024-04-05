# topshiriq30. Ikkita butun A va B solari berilgan. 
# Jumlani rostlikka tekshiring: "A va B sonlaring faqat bittasi toq son".

print("A = ")
A = int(input())
print("B = ")
B = int(input())
if (A % 2 != 0 and B % 2 == 0) or (A % 2 == 0 and B % 2 != 0) :
    print("True")
else :
    print("False")