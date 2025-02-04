def kidsWithCandies(candies, extraCandies):
    max_ = max(candies)

    result = []

    for i in candies:
        if i + extraCandies >= max_:
            result.append(True)
        else:
            result.append(False)

    return result

result = kidsWithCandies([2,3,5,1,3],3)
print(result)