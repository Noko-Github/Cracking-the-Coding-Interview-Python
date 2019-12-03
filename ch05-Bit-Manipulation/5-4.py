def get_next(num):
    bit = num
    c0 = 0
    c1 = 0
    while (bit & 1 == 0) and (bit != 0):
        c0 += 1
        bit >>= 1

    while (bit & 1) == 1:
        c1 += 1
        bit >>= 1

    if c0+c1 == num or c0+c1 == 0:
        return None

    num |= 1 << c0+c1
    num &= ~((1 << c0+c1) - 1)
    num |= (1 << (c1-1)) - 1
    return num


def get_prev(num):
    bit = num
    c0 = 0
    c1 = 0
    while (bit & 1 == 0) and (bit != 0):
        c0 += 1
        bit >>= 1

    while (bit & 1) == 1:
        c1 += 1
        bit >>= 1

    if c0+c1 == num or c0+c1 == 0:
        return None

    num &= ~((1 << c0+c1) - 1)
    num |= ((1 << c1) - 1) << (c0-1)


num = 13948
print(get_next(num))
print(get_prev(num))
