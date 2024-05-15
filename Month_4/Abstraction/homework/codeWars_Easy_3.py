import os
os.system("clear")

# CodeWars Degree 7

def sort_my_string(s):
    res_even = ""
    res_odd = ""
    for x in range(len(s)):
        if x % 2 == 0:
           res_even += s[x]
        else :
            res_odd += s[x] 
    return res_even + " " + res_odd

print(sort_my_string("CodeWars"))