# topshiriq34, Uchta A, B, C butun sonlar berilgan. 
# Jumlani rostlikka tekshiring: "A, B, C sonlaridan faqat bittasi musbat son"


print("A = ")
A = int(input())
print("B = ")
B = int(input())
print("C = ")
C = int(input())
if (A > 0 and B < 0 and C < 0) or (A < 0 and B > 0 and C < 0) or (A < 0 and B < 0 and C > 0) :
    print("True")
else :
    print("False")