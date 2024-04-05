# Berilgan ro'yxatda elementlarni o'sish , kamayish yoki tartibsiz joylashganini aniqlovchi dastur tuzing.

# Input: [5,3,8,1]
# Output: tartibsiz

# Input: [1,4,7,9]
# Output: o'sish

massiv = list(map(int,input("Elementlarni kiriting : ").split()))

sored = massiv.copy()
sored.sort()
reversed = sored.copy()
reversed.reverse()

if massiv == sored:
    print("o'sish")
elif massiv == reversed:
    print("kamayish")
else :
    print("tartibsiz")

