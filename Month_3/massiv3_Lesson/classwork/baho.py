baho = int(input())
if (baho // 5 + 1) * 5 - baho < 3 and baho >= 38:
	baho = (baho // 5 + 1) * 5
else:
    baho = baho
print(baho)