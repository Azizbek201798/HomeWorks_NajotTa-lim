# Task - 4; 844 - Backspace-string-compare;

# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

# Example 1:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# Example 2:

# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
# Example 3:

# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b"

class Solution(object):
    def backspaceCompare(self, s, t):
        ss=[]
        tt=[]
        for i in t :
            if i=='#'and len(tt)!=0:
                tt.pop()
            if i!='#':
                tt.append(i)
        for i in s:
            if i=='#' and len(ss)!=0:
                ss.pop()
            if i!='#':
                ss.append(i)
        return ss==tt

