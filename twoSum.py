def twoSum(array, target):

    hash_table = {}

    for x in array:
        if (target - x) in hash_table:
            return [x,target-x]
        else:
            hash_table[x] = True

    return []


print(twoSum([2, 7, 11, 15], 9))
