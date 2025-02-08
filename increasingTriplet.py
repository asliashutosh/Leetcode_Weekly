def increasingTriplet(nums):

    first = second = float('inf')

    for i in nums:
        if i<=first:
            first = i
        elif i<=second:
            second = i
        else:
            return True

    return False


print(increasingTriplet([20,100,10,12,5,13]))
