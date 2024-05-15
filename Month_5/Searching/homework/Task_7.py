# Task - 2529; Maximum-count-of-positive-integer-and-negative-integer

# Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers 
# and the number of negative integers.

# In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, 
# then return the maximum of pos and neg.
# Note that 0 is neither positive nor negative.

# Example 1:

# Input: nums = [-2,-1,-1,1,2,3]
# Output: 3
# Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.

class Solution(object):
    def maximumCount(self, nums):
        self.nums = nums

        count_pos = 0
        count_neg = 0
        for x in self.nums:
            if x > 0:
                count_pos += 1
            elif x < 0:
                count_neg += 1
        if count_pos > count_neg:
            return count_pos
        else:
            return count_neg