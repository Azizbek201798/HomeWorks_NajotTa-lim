# Task - 2824. Count Pairs Whose Sum is Less than Target

# Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) 
# where 0 <= i < j < n and nums[i] + nums[j] < target. 

# Example 1:

# Input: nums = [-1,1,2,3,1], target = 2
# Output: 3
# Explanation: There are 3 pairs of indices that satisfy the conditions in the statement:
# - (0, 1) since 0 < 1 and nums[0] + nums[1] = 0 < target
# - (0, 2) since 0 < 2 and nums[0] + nums[2] = 1 < target 
# - (0, 4) since 0 < 4 and nums[0] + nums[4] = 0 < target

class Solution(object):
    
    def countPairs(self, nums, target):
        nums.sort()
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    count += 1
        return count