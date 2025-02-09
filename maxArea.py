def maxArea(height):
    res = 0

    leftPointer = 0
    rightPointer = len(height) - 1

    while leftPointer < rightPointer:

        area = (rightPointer - leftPointer) * min(height[leftPointer], height[rightPointer])
        res = max(res, area)

        if height[leftPointer] < height[rightPointer]:
            leftPointer += 1
        else:
            rightPointer -= 1
    return res

print(maxArea([1,8,6,2,5,4,8,3,7]))