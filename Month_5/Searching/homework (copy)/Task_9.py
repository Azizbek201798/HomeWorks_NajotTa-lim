# Task - 268; Missing-number

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that 
# is missing from the array.
# 
# Example 1: 
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number 
# in the range since it does not appear in nums.

# Example 2:
# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the 
# range since it does not appear in nums.

class Solution(object):
    def missingNumber(self, nums):
        self.nums = nums
        k = 0
        while 1:
            if k in self.nums:
                k += 1
                continue
            else:
                return k  