# Topshiriq_14 => DONE by LeoMessi

# Ikkita dictionary ma'lumotlarini keyslari bir xillarini qiymatlarini yig'indisini olib barcha elementlarni birlashtiring.
# Input:
# d1 = {'a': 100, 'b': 200, 'c':300,'k' : 1000}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Output: D={'a': 400, 'b': 400, 'd': 400, 'c': 300,'k' = 1000}
# #topshiriq_dict_and_list

import os
os.system("clear")

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d1_keys = list(d1.keys())
d2_keys = list(d2.keys())
d1_val = list(d1.values())
d2_val = list(d2.values())
d_total = {}
print(f"d1 : {d1}")
print(f"d2 : {d2}")

for x in range(3):
    if d1_keys[x] == d2_keys[x]:
        d_total.update({d1_keys[x]:d1[d1_keys[x]] + d2[d2_keys[x]]})
    else :
        d_total.update({d1_keys[x]:{d1[d1_keys[x]]}})
        d_total.update({d2_keys[x]:{d2[d2_keys[x]]}})

print(f"d_total : {d_total}")