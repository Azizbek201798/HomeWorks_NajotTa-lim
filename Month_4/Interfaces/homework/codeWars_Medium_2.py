# TASK - 2 => DONE by Azizbek

# You are given an array asteroids of integers representing asteroids in a row.
# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed. There won't be any 0 in the given list.
# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

# Examples
# ([-2, -1, 1, 2]) ➞ [-2, -1, 1, 2]
# ([-2, 1, 1, -2]) ➞ [-2, -2]
# ([1, 1, -2, -2]) ➞ [-2, -2]
# ([10, 2, -5]) ➞ [10]
# ([8, -8]) ➞ []
# ([]) ➞ []

def asteroid_collision(asteroids):
    massiv = []

    for asteroid in asteroids:
        if asteroid > 0:
            massiv.append(asteroid)
        else:
            while massiv and massiv[-1] > 0 and massiv[-1] < abs(asteroid):
                massiv.pop()

            if not massiv or massiv[-1] < 0:
                massiv.append(asteroid)
            elif massiv[-1] == abs(asteroid):
                massiv.pop()

    return massiv