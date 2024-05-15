import os
os.system("clear")

def operations(number):
    count = 0

    while number > 0:
        if number % 2 == 0:
            number //= 2
        else:
            number -= 1
        count += 1

    return count