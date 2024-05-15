# CodeWars_Medium_2 => DONE BY Azizbek;

# In this kata you have to correctly return who is the "survivor", ie: the last element of a Josephus permutation.
# Basically you have to assume that n people are put into a circle and that they are eliminated in steps of 
# k elements, like this:

# n=7, k=3 => means 7 people in a circle
# one every 3 is eliminated until one remains
# [1,2,3,4,5,6,7] - initial sequence
# [1,2,4,5,6,7] => 3 is counted out
# [1,2,4,5,7] => 6 is counted out
# [1,4,5,7] => 2 is counted out
# [1,4,5] => 7 is counted out
# [1,4] => 5 is counted out
# [4] => 1 counted out, 4 is the last element - the survivor!
# The above link about the "base" kata description will give you a more thorough insight about the origin 
# of this kind of permutation, but basically that's all that there is to know to solve this kata.

import os
os.system("clear")

def josephus_survivor(total,k):
    people = []

    for x in range(1,total+1):
        people.append(x)

    k -= 1
    index = k % len(people)

    while len(people) > 1:
        people.pop(index)
        index = (index + k) % len(people)

    return people[0]