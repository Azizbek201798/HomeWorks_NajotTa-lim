# Task - 3; 387 - First-unique-character-in-a-string;

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# 
# Example 1:
# 
# Input: s = "leetcode"
# Output: 0
# Example 2:
# 
# Input: s = "loveleetcode"
# Output: 2
# Example 3:
# 
# Input: s = "aabb"
# Output: -1

# import os
# os.system("clear")

import os
os.system("clear")

class Solution(object):
    def firstUniqChar(self, s):
        dc = {}
        for x in s:
            if x not in dc:
                dc[x] = 1
            else: 
                dc[x] += 1
        index = -1
        for x in range(len(s)):
            if dc[s[x]] == 1:
                index = x
                break
        return index

app = Solution()
print(app.firstUniqChar("leetcode"))