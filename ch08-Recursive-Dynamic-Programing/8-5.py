def min_product(a, b):
    bigger = a if a > b else b
    smaller = a if a < b else b
    return min_product_helper(smaller, bigger)


def min_product_helper(smaller, bigger):
    print('smaller:{}, bigger:{}'.format(smaller, bigger))
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger

    s = smaller >> 1
    halfProd = min_product_helper(s, bigger)
    print('halfProd:{}'.format(halfProd))

    if smaller % 2 == 0:
        return halfProd + halfProd
    else:
        return halfProd + halfProd + bigger


a = 8
b = 6
print(min_product(a, b))
