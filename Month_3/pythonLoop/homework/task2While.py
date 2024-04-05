# ***Topshiriq2***
# while yordamida k dan n gacha sonlar ichidan 3 ga bo'linadigan biroq 5 ga bo'linmaydigan sonlar yig'indisini topish 
# algoritmini ishlab chiqing

# DONE

k = int(input("k = "))
n = int(input("n = "))
sum = 0
for k in range(n):
    if k % 3 == 0 and k % 5 != 0:
        sum += k
print("k dan n gacha 3 ga bo'linadigan 5 ga bo'linmaydigan sonlar yig'indisi = ", sum)
