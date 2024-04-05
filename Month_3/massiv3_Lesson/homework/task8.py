# Topshiriq_8 => DONE by LeoMessi

#  3ta dictionary ma'lumotlarini bitta dictionaryga birlashtiring.
# Input:
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50, 6:60}
# Output: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

import os
os.system("clear")

# 1-USUL

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
dictUniversal = {}

dictUniversal.update(dic1)
dictUniversal.update(dic2)
dictUniversal.update(dic3)

print(dictUniversal)

# 2-USUL

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50, 6:60}
# dictUniversal = {}

# for x in dic1:
#     dictUniversal.update({x : dic1[x]})

# for x in dic2:
#     dictUniversal.update({x : dic2[x]})

# for x in dic3:
#     dictUniversal.update({x : dic3[x]})

# print(dictUniversal)
