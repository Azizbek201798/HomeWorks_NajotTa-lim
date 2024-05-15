# Task - 2089. Find-target-indices-after-sorting-array

# You are given a 0-indexed integer array nums and a target element target.
# A target index is an index i such that nums[i] == target.
# Return a list of the target indices of nums after sorting nums in non-decreasing order. 
# If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

# Example 1:

# Input: nums = [1,2,5,2,3], target = 2
# Output: [1,2]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The indices where nums[i] == 2 are 1 and 2.

class Solution(object):
    def targetIndices(self, nums, target):
        self.nums = sorted(nums)
        self.target = target
        res = []
        for x in range(len(self.nums)):
            if self.nums[x] == self.target:
                res.append(x)
        return res