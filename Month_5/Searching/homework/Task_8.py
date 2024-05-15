# Task - 1385; Find-the-distance-value-between-two-arrays

# Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.
# The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

# Example 1:

# Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
# Output: 2
# Explanation: 
# For arr1[0]=4 we have: 
# |4-10|=6 > d=2 
# |4-9|=5 > d=2 
# |4-1|=3 > d=2 
# |4-8|=4 > d=2 
# For arr1[1]=5 we have: 
# |5-10|=5 > d=2 
# |5-9|=4 > d=2 
# |5-1|=4 > d=2 
# |5-8|=3 > d=2
# For arr1[2]=8 we have:
# |8-10|=2 <= d=2
# |8-9|=1 <= d=2
# |8-1|=7 > d=2
# |8-8|=0 <= d=2

class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        self.arr1 = arr1
        self.arr2 = arr2
        self.d = d

        count = 0
        for x in self.arr1:
            check = False
            for y in self.arr2:
                if abs(x-y) <= self.d:
                    check = True
                    break
            if check == False:
                count += 1
        return count
        