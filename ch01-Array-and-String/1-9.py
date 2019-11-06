def is_rotation(s1, s2):
    if len(s1) != len(s2) or s1 is None or s2 is None:
        return False

    s1s1 = s1 + s2
    if s2 in s1s1:
        return True

    return False


s1 = 'waterbottle'
s2 = 'erbottlewat'

print(is_rotation(s1, s2))
