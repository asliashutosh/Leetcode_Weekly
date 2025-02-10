"""
This module contains the implementation of the max_operations function.
"""

def max_operations(array, k):
    """
    Finds the maximum number of pairs in the array whose sum equals k.
    """
    array.sort()
    n = len(array)
    count = 0

    l = 0
    r = n - 1

    while l < r:
        if array[l] + array[r] == k:
            count += 1
            l += 1
            r -= 1
        elif array[l] + array[r] < k:
            l += 1
        else:
            r -= 1

    return count

print(max_operations([1, 2, 3, 4], 5))
