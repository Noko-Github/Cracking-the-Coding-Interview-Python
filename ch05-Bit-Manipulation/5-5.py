def bit_swap_required(a, b):
    count = 0
    for diff in bin(a ^ b)[2:]:
        if diff:
            count += 1

    return count


a = 5   # 0101
b = 10  # 1010
print(bit_swap_required(a, b))
