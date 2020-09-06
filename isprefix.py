# abcd => ab ==> true
# wxyz => xy ==> false


def isprefix(string, prefix):
    if len(prefix) > len(string):
        return False

    # i=0
    # while i<len(prefix):
    #     if prefix[i] != string[i]:
    #         return False
    #     i += 1
    # return True

    for i in range(len(prefix)):
        if prefix[i] == string[i]:
            continue        # return true
        else:
            return False

    return True


print(isprefix("abcd", "abcd"))
print(isprefix("abcd", "ab"))
print(isprefix("abcd", "ac"))
