def maxVowels(string, k):

    n = len(string)
    max_vowel,count = 0, 0
    vowels = {'a','e','i','o','u', 'A','E','I','O','U'}


    for i in range(k):

        if string[i] in vowels:
            count += 1

    max_vowel = count

    for i in range(k,n):

        if string[i-k] in vowels:
            count -= 1
        if string[i] in vowels:
            count += 1

        max_vowel = max(max_vowel,count)

    return max_vowel

print(maxVowels("abciiidef",3))