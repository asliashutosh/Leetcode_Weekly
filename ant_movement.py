def antMovement(array):

    result = 0
    startingPostion = 0

    for i in array:
        result += i
        if result==0:
            startingPostion += 1

    return startingPostion

result = antMovement([1,1,1,1,1])
print(result)