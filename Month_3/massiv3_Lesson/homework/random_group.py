import random
import os
os.system("clear")

def divide_players(players):
    random.shuffle(players)
    group_a = players[:len(players)//2]
    group_b = players[len(players)//2:]
    return group_a, group_b

# Example usage
all_players = ['Begzod', 'Azizbek', 'Akbarshoh', 'Haqnazar', 'Nodir', 'Olimjon', 'Abdullo',"Fozil", 'Sardor', 'Abdulboriy']
group_a_players, group_b_players = divide_players(all_players)
print("Group A Players:", group_a_players)
print("Group B Players:", group_b_players)