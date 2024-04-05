a1,a2,a3,a4,a5,a6,a7 = map(int,input().split())
S = int(input())
sum = a1+a2+a3+a4+a5+a6+a7
if S > sum:
	print(S - sum)
else :
	print(0)  