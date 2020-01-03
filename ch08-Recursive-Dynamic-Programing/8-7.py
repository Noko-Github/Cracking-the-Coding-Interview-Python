def get_perms(string):
    permutations = []

    if string is None:
        return None

    if len(string) == 0:
        permutations.append(" ")
        return permutations

    first = string[0]
    remainder = string[1:]
    words = get_perms(remainder)
    print(words)
    for word in words:
        print('word:{}'.format(word))
        i = 0
        for _ in word:
            # print(word)
            # print(first)
            s = insert_char_at(word, first, i)
            permutations.append(s)
            i += 1

    return permutations


def insert_char_at(word, c, i):
    start = word[0:i]
    end = word[i:]
    print('-----------------------')
    print('start:{}'.format(start))
    print('c:{}'.format(c))
    print('end:{}'.format(end))
    print(start+c+end)
    print('-----------------')
    return start + c + end


string = 'abc'
print(get_perms(string))
