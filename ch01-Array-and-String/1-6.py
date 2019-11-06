def compress(string):
    tmp = None
    result = ''
    count = 0
    for char in string:

        if tmp is None:
            tmp = char

        if tmp != char:
            result += tmp
            tmp = char
            result += str(count)
            count = 0
        count += 1
    result += string[-1]
    result += str(count)
    return result


target = 'aaaacccdddde'
result = compress(target)
print(result)
