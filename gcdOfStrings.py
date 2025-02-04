def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

def gcdOfStrings(string1, string2):

    if string1 + string2 != string2 + string1:
        return ""

    return string1[:gcd(len(string1),len(string2))]


result = gcdOfStrings("ABABAB","ABAB")
print(result)

