import os
os.system("clear")

x1,y1,x2,y2 = map(int,input("Koordinatalarni kiriting : ").split())

time = max(abs(x1-x2),abs(y1-y2)) * 0.5
print(time)