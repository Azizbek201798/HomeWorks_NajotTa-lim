ls = list(map(int,input().split()))

maxlar = ls.copy()
maxlar.remove(min(ls))
minlar = ls.copy()
minlar.remove(max(ls))

print(sum(minlar),sum(maxlar))
