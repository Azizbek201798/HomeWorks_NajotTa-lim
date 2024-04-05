# List ichidagi elementlarni palindromligini aniqlaydigan dastur tuzing.
#   ["ada", 212, False, 4567, "aziza"]
#   ada - > palindrom
#   212 - > palindrom
#   False - > palindrom emas
#   4567 - > palindrom emas
#   'aziza' - > palindrom

k = ["anvar","kakak",12345,True,"amma","aziza"]
for x in k:
    z = str(x)[::-1]
    if x == z:
        print(x ,"-> palindrom")
    else :
        print(x,"-> palindrom emas")
