def canPlaceFlowers(flowerbed,n):

    # So we'll iterate through all the elements
    # Checking if [i]th is 0 as soon as we get the 0
    # we will check there adjacent meaning left and right
    # If both are 0 then we will add 1 in flowerbed[i]th location
    # And reduce the count of n
    # Lastly we will check if n != 0 will throw false else true

    for i in range(0, len(flowerbed)):

        if flowerbed[i] == 0:

            leftSideEmpty = (i==0) or (flowerbed[i-1] == 0)
            rightSideEmpty = (i==len(flowerbed) - 1) or (flowerbed[i+1]==0)

            if leftSideEmpty and rightSideEmpty:
                flowerbed[i] = 1
                n -= 1

    return True if n<=0 else False


result = canPlaceFlowers([0,0,1,0,0],1)
print(result)