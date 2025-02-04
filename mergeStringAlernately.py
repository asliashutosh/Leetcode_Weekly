# Approach
# First take the common length of both the string and traverse till common length
# Find out which word has the longest string
# Append the rest in the result using the concept Concatenating

# def mergeString(String1, String2):
#
#     lengthOfString1 = len(String1)
#     lengthOfString2 = len(String2)
#
#     CommonLength = lengthOfString1 if lengthOfString1<=lengthOfString2 else lengthOfString2
#
#     result = []
#
#     for i in range(0,CommonLength):
#         result.append(String1[i])
#         result.append(String2[i])
#
#     if (lengthOfString1>lengthOfString2):
#         result.append(String1[len(String2)::])
#     else:
#         result.append(String2[len(String1)::])
#
#     result = "".join(result)
#
#     return result
#
# result = mergeString('abcd','pq')
# print(result)


def mergeString(String1, String2):

    lengthOfString1 = len(String1)
    lengthOfString2 = len(String2)

    CommonLength = lengthOfString1 if lengthOfString1<=lengthOfString2 else lengthOfString2

    result = ''

    for i in range(0,CommonLength):
        result += String1[i]
        result += String2[i]
        # result.append(String1[i])
        # result.append(String2[i])

    if (lengthOfString1>lengthOfString2):
        result += String1[len(String2)::]
        # result.append(String1[len(String2)::])
    else:
        result += String2[len(String1)::]
        # result.append(String2[len(String1)::])

    # result = "".join(result)

    return result

result = mergeString('abc','pqr')
print(result)





# def myrs(str1,str2):
#     res=[]
#     l1 = len(str1)
#     l2 = len(str2)
#     cl = l1 if l1<=l2 else l2
#     for i in range(0,cl):
#         res.append(str1[i])
#         res.append(str2[i])
#         l1-=1
#         l2-=1
#     if l1 :
#         for i in range(len(str1)-l1,len(str1)):
#             res.append(str1[i])
#     else :
#         for i in range(len(str2)-l2,len(str2)):
#             res.append(str2[i])
#     return res
#
#
#
# result = myrs("abc","pqr")
# print(result)