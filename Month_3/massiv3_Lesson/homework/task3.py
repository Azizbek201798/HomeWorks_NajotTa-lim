# Topshiriq_3 => DONE by LeoMessi

# Dictionary berilgan ushbu dictionaryda kaliti juft oâ€™rindagi qiymatlarni kaliti toq oâ€™rindagi 
# bilan almashtiradigan va chiqaradigan funksiya yarating. 
# Input (Kiruvchi maâ€™lumotlar):
# dict1={1:ABC, 2:DEF, 3:GHI, 4:JKL, 5:MNO}
# Output (Chiquvchi maâ€™lumotlar):
# dict1={1:DEF, 2:ABC, 3:JKL, 4:GHI, 5:MNO}

import os
os.system("clear")

dict1={1:'ABC', 2:'DEF', 3:'GHI', 4:'JKL', 5:'MNO'}
print(f"Before : {dict1}")

for x in dict1:
    if x % 2 == 0:
        temp = dict1[x]
        dict1.update({x:dict1[x-1]})
        dict1.update({x-1:temp})

print(f"After  : {dict1}")

