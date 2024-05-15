import math
import os
os.system("clear")

# CodeWars Degree 7

def cooking_time(needed_power, minutes, seconds, power) -> str:
    total = math.ceil((int(needed_power[:-1]) / int(power[:-1])) * (minutes * 60 + seconds))
    return f"{(total // 60)} minutes {(total) % 60} seconds"

print(cooking_time("600W",4,20,"800W"))
print(cooking_time("83W",61,80,"26W"))
print(cooking_time("7500W",0,5,"600W"))
print(cooking_time("21W",64,88,"25W"))