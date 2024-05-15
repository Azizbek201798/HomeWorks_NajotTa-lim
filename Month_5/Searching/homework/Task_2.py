# Task - 1351. Count-negative-numbers-in-a-sorted-matrix

# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, 
# return the number of negative numbers in grid.

# Example 1:

# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.

class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        count = 0
        for x in self.grid:
            for y in x:
                if y < 0:
                    count += 1
        return count