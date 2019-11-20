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

    if c0+c1 == len(num) or c0+c1 == 0:
        return None


def get_prev(num):
    pass


num = 13948
print(get_next(num))
