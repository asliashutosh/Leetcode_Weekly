def isSubsequence(s,t):

    firstPointer = 0
    secondPointer = 0

    while firstPointer<len(s) and secondPointer<len(t):
        if s[firstPointer] == t[secondPointer]:
            firstPointer += 1
        secondPointer += 1

    if firstPointer==len(s):
        return True
    else:
        return False

print(isSubsequence("abc", "ahbgdc"))