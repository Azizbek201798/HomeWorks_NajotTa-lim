# Task - 349. Intersection-of-two-arrays

# Given two integer arrays nums1 and nums2, return an array of their 
# intersection.Each element in the result must be unique and you may return the result in any order.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

class Solution(object):
    def intersection(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
        res = []
        for x in self.nums1:
            if x in self.nums2 and x not in res:
                res.append(x)
        return res