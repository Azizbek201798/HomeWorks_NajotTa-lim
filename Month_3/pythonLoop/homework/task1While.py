# ***Topshiriq1***
# while yordamida n!(o'zigacha bo'lgan sonlar ko'paytmasi) topish algoritmini ishlab chiqing M: 5!=120

# DONE

son = int(input("Sonni kiriting : "))
fact, n = 1, 1
while son > 0:
    fact *= n
    n += 1
    son -= 1
print(n - 1,"! = ",fact,sep = "")