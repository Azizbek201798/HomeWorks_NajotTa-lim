# P1:

# Ikkita listning o'rta arifmetigini chiqaring.

# Input:
# [1, 1, 3, 4, 4, 5, 6, 7]
# [0, 1, 2, 3, 4, 4, 5, 7, 8]

# Output:
# 3.823529411764706

ls1 = [10, 1, 3, 4, 4, 5, 6, 7]
ls2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]
count,sumTotal,avg = 0,0,0

sum1 = sum(ls1)
count1 = len(ls1)
sum2 = sum(ls2)
count2 = len(ls2)
avg = (sum1+sum2)/(count1+count2)
print(avg)