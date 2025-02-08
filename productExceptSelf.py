def multiplyForUs(array):
    res = 1
    for i in range(len(array)):
        res = res* array[i]
    return res

def removeForUs(array, index):
    result = []
    for i in range(len(array)):
        if i!=index:
            result.append(array[i])
    return result

def productExceptSelf(nums):
    result = []
    for i in range(len(nums)):
        array = removeForUs(nums,i)
        result.append(multiplyForUs(array))
    return result

print(productExceptSelf([-1,1,0,-3,3]))

# The above solution is not the best approch although it delivers the answer in O(n^2) Time Complexity
# Better approch is to use prefix-sufix approch


def productOfArrayExceptSelf(array):

    n = len(array)
    result = [1]*n

    prefix,suffix = 1,1

    for i in range(n):
        result[i] = prefix
        prefix = prefix * array[i]

    for i in range(n-1,-1,-1):
        result[i] = result[i] * suffix
        suffix = suffix* array[i]

    return result

print(productOfArrayExceptSelf([1,2,3,4]))


