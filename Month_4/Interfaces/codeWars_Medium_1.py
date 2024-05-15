import os
os.system("clear")

def count_presents(prod : dict, presents : list) -> int:
    
    Total_time = sum(prod.values()) * 24 * 3600
    
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
