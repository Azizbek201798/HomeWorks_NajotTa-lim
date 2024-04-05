# Satr uzunligi 2 va undan ortiq, birinchi va oxirgi belgilari bir xil 
# bo‘lgan satrlar sonini hisoblavchi Python dasturini yozing. 
#   Namuna roʻyxati : ['abc', 'xyz', 'bo'lib','aba', '1221']  
#   Kutilayotgan natija: 3
import os 
os.system("clear")

k = ["anvar","123451",343,True,"inni"]
count = 0
print("Elements : ", end = "")
for x in k:
    z = str(x)
    if z[0] == z[len(z)-1]:
        print(z,end = ", ")
        count += 1
print("\nSoni = ",count)