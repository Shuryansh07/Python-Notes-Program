def getStr(s):
    strlen = len(s)
    newStr = ''
    for i in range(strlen):
        newStr += s[i] * 3
    strlen = len(newStr)
    return [newStr,strlen]

print(getStr("abc"))



