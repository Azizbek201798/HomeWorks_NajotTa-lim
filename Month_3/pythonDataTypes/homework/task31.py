# topshiriq31. Ikkita butun A va B solari berilgan. 
# Jumlani rostlikka tekshiring: "A va B sonlarining har ikkalasi ham yoki toq son yo ki juft son"

print("A = ")
A = int(input())
print("B = ")
B = int(input())
if (A % 2 == 0 and B % 2 == 0) or (A % 2 != 0 and B % 2 != 0) :
    print("True")
else :
    print("False")