import os
import math
os.system("clear")

def calculate_minimum_time(n, m):
    rounds = math.ceil(n / m)  # Number of rounds required to cook all the pancakes
    time_per_round = 2  # Each round takes 2 minutes (1 minute per side)
    remaining_pancakes = n % m  # Number of pancakes in the last round
    
    total_time = (rounds - 1) * time_per_round  # Time for the majority of the pancakes
    
    if remaining_pancakes > 0:
        total_time += time_per_round + (remaining_pancakes - 1) * 2  # Time for the remaining pancakes
    
    return total_time

# Example usage
n = 15  # Number of pancakes
m = 3   # Maximum pancakes on the frying pan at a time

minimum_time = calculate_minimum_time(n, m)
print(f"The minimum time required to cook {n} pancakes, with a maximum of {m} pancakes at a time, is {minimum_time} minutes.")