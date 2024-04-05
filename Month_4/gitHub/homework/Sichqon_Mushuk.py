import os
os.system("clear")

a,b,c = map(int,input().split())
if abs(a - c) == abs(b - c):
  print("sichqon")
elif abs(a - c) > abs(b - c):
  print("2-mushuk")
else:
  print("1-mushuk")