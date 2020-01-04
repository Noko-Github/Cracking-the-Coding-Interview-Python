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
    return start + c + end


def get_perms_(string):
    permutations = []
    result = []
    if len(string) == 0:
        permutations.append(" ")
        return permutations

    i = 0
    for _ in string:
        before = string[0:i]
        after = string[i+1:]
        perms = get_perms_(before+after)

        for s in perms:
            result.append(string[i]+s)
        i += 1

    return result


string = 'abc'
print(get_perms_(string))
