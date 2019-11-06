def permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    array = [0]*256
    for char in str1:
        array[ord(char)] += 1

    for char in str2:
        array[ord(char)] -= 1
        if array[ord(char)] < 0:
            return False

    return True


str1 = 'aabbcc'
str2 = 'abcabc'

print(permutation(str1, str2))
