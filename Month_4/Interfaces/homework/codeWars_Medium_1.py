import os
os.system("clear")

def count_presents(prod, presents):
    total_workload = sum(prod.values())
    total_present_time = sum([int(present.split(':')[0]) for present in presents])
    
    if total_workload == 0 or total_present_time == 0:
        return 0
    
    return total_workload // total_present_time

print(count_presents({"Santa": 1, "elf_1": 1, "elf_2": 2},["01:00:00", "06:00:00", "12:00:00", "18:00:00", "24:00:00", "36:00:00"]))