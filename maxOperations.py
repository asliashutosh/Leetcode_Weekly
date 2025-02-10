def maxOperations(array, k):

    array.sort()
    n = len(array)
    count = 0

    l = 0
    r = n-1

    while l<r:

        if array[l] + array[r] == k:
            count += 1
            l += 1
            r -= 1
        elif array[l] + array[r] < k:
            l += 1
        else:
            r -= 1

    return count

print(maxOperations([1,2,3,4], 5))