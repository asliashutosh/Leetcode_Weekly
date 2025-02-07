def reverseWords(s):
    s = s.split(" ")
    res = []
    for i in s:
        if i != '':
            res.append(i.strip())

    return " ".join(res[::-1])


res = reverseWords("The World is reversed")
print(res)