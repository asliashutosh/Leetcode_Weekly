def longestSubarray(nums):

    max_width = 0
    num_zeros = 0
    n = len(nums)
    left = 0

    # [0, 1, 1, 1, 0, 1, 1, 0, 1]

    for right in range(n):
        if nums[right] == 0:
            num_zeros += 1

        while num_zeros > 1:
            if nums[left] == 0:
                num_zeros -= 1

            left += 1

        width = right - left + 1

        max_width = max(max_width,width)

    return max_width - 1

print(longestSubarray([1,1,0,1]))