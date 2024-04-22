# Task - 2 -> DONE by Azizbek

# Given an array of integers, remove the n smallest. If there are multiple elements with the same value,
# remove the ones with a lower index first. If n is greater than the length of the array/list,
# return an empty list/array. If n is zero or less, return the original array/list.
# Don't change the order of the elements that are left.

# Examples
# remove_smallest ((-10), [1,2,3,4,5]) = [1,2,3,4,5]
# remove_smallest (0, [1,2,3,4,5]) = [1,2,3,4,5]
# remove_smallest (2, [5,3,2,1,4]) = [5,3,4]
# remove_smallest (3, [5,3,2,1,4]) = [5,4]
# remove_smallest (3, [1,2,3,4,5]) = [4,5]
# remove_smallest (5, [1,2,3,4,5]) = []
# remove_smallest (9, [1,2,3,4,5]) = []
# remove_smallest (2, [1,2,1,2,1]) = [2,2,1]

import os
os.system("clear")

def remove_smallest(n, arr):
    if n <= 0:
        return arr
    if n >= len(arr):
        return []

    # Tayyor saralash methodi.
    sorted_arr = sorted(arr)
    for _ in range(n):
        min_val = sorted_arr[0]
        arr.remove(min_val)
        sorted_arr.remove(min_val)

    return arr
