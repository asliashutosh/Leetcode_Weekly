# Better Approch is Two Poiners

def reverseVowels(string):

    arrayOfVowels = {"A","E", "I", "O", "U", 'a', 'e', 'i', 'o', 'u'}
    reversedChar = []
    requiedString = list(string)
    count = 0

    for i in string:
        if i in arrayOfVowels:
            reversedChar.append(i)

    reversedChar = reversedChar[::-1]

    for i in range(len(requiedString)):
        if requiedString[i] in arrayOfVowels:
            requiedString[i] = reversedChar[count]
            count += 1


    return "".join(requiedString)

result = reverseVowels("IceCreAm")
print(result)