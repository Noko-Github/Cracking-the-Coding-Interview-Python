def print_binary(num):
    result = []
    for i in range(2, 34, 2):
        bit = int(num // (1/i))
        num = num % (1/i)
        result.append(bit)

    return result


print(print_binary(0.1255))
