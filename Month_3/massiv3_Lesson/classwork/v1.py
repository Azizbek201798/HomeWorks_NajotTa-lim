# V1:
# Foydalanuvchi istalgancha son kiritadi. Siz esa bir marta dublikat son kiritishi bn input jarayonini tugating 
# va ekranga kiritilgan sonlarni chiqaring.
# Faqat set ishlatilsin!

import os
os.system("clear")

st = set()

while True:
    number = int(input("Son = "))
    if number not in st:
        st.add(number)
    else:
        break
print(st)
