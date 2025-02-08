def compress(chars):
    read, write = 0, 0
    n = len(chars)

    while (read < n):
        char = chars[read]
        count = 0

        while (read < n and chars[read] == char):
            count += 1
            read += 1

        chars[write] = char
        write += 1

        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1

    return write

print(compress(["a","a","b","b","c","c","c"]))

# The above one is optimal solution but I have one more
# But I don't know why leetcode is not accepting

def compressBruteForce(array):
    hashTable = {}
    reversed_num = 0
    digit = 0

    result = []

    for i in array:
        if i in hashTable:
            hashTable[i] += 1
        else:
            hashTable[i] = 1

    for j in (hashTable):
        result.append(j)
        if hashTable[j] == 1:
            continue

        if hashTable[j] >= 10:
            while (hashTable[j] != 0):
                digit = hashTable[j] % 10
                reversed_num = reversed_num * 10 + digit
                result.append(str(digit))
                hashTable[j] //= 10


        else:
            result.append(str(hashTable[j]))

    return len(result)


print(compressBruteForce(["a", "a", "b", "b", "c", "c", "c"]))
