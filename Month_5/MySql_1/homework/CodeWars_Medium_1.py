# Task - 1 => CodeWars_Medium_1

# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example: 
# expanded_form(1298) # Should return '1000 + 200 + 90 + 8'
# expanded_form(421) # Should return '400 + 20 + 1'
# expanded_form(70304) # Should return '70000 + 300 + 4'

import os
os.system("clear")

def expanded_form(son : int):
    son_str = str(son)    
    length = len(son_str)    
    massiv = []
    
    for i in range(length):
        raqam = int(son_str[i])
        
        if raqam != 0:
            a = raqam * 10**(length - i - 1)            
            massiv.append(str(a))
    
    massiv_str = ' + '.join(massiv)
    
    return massiv_str

print(expanded_form(10010))