# V4:
# Foydalanuvchi string kiritadi. Shu stringdagi har bitta belgidan nechtadan borligini dictionary ga quyidagicha joylang:
# Input:     "w3resource"
# Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

my = input("Satr kiriring : ")
k = {}

for x in my:
    if x in k:
        k[x] += 1
    else :
        k[x] = 1

print(k)






