# TASK 1 => DONE by Azizbek 

# Christmas Present Calculator
# After we find out if Santa can save Christmas there is another task to face.
# Santa's little helper aren't sick anymore. They are ready to give away presents again. But some of them are still weak.
# This leads to more productive elves than others.

# How many presents can Santa distribute this christmas?

# Your Task:
# You will get two inputs.
# One dictionary with the producitivity of each elf like the following:

# {"Santa": 1, "elf_1": 1, "elf_2": 1, "elf_3": 2, "elf_4": 3}

# and a string array with the time needed for each present like the following:

# "hh:mm:ss"

# The productivity describes the workload an elf can do each day:

# productivity 1 = 24 hours each day
# productivity 2 = 48 hours each day
# ...

# Return the number of present they can distribute at maximum.

# Note that:

# They have only 24 hours
# They try to give out as much as presents as possible (the ones with less time first)
# All the elves can work on multiple tasks. You can count it as one work capacity

import os
os.system("clear")

def count_presents(prod : dict, presents : list) -> int:
    
    # Jami ishlay olish vaqti:
    Total_time = sum(prod.values()) * 24 * 3600
    
    # Jami ishlatilgan vaqt
    Surfed_time = 0
    count = 0

    def sort_presents(time : list) -> list:
        hour,min,sec = map(int,time.split(":"))
        return hour * 3600 + min * 60 + sec

    sorted_time = sorted(presents, key = sort_presents)

    for present_time in presents:
        time = present_time.split(":")
        Surfed_time += int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
        if Surfed_time > Total_time:
            return f"Jami : {count} ta sovg'ani tarqata olishadi!"
        count += 1

print(count_presents({"Santa": 1, "elf_1": 1, "elf_2": 2},["01:10:00", "06:09:00", "12:00:00", "18:00:00", "24:00:00", "36:00:00"]))