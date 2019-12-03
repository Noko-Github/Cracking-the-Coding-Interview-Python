def flip_bit(n):
    bit_n = bin(n)
    target = 0
    count = 0
    result = []
    # for bit in bit_n[:1:-1]:
    for bit in [1, 1, 1, 1, 0, 1, 1, 1,  0, 1, 1]:
        if bit != target:
            result.append(count)
            count = 0
            target = (0 == target)
        count += 1
    result.append(count)

    max_seq = 1
    print(result)
    for i in range(0, len(result), 2):
        zero_seq = result[i]
        ones_seq_left = result[i-1] if i - 1 >= 0 else 0
        ones_seq_right = result[i+1] if i + 1 < len(result) else 0

        this_seq = 0
        if zero_seq == 1:
            this_seq = 1 + ones_seq_left + ones_seq_right
        elif zero_seq > 1:
            this_seq = 1 + max(ones_seq_right, ones_seq_right)
        elif zero_seq == 0:
            this_seq = max(ones_seq_right, ones_seq_left)

        max_seq = max(this_seq, max_seq)

    print(max_seq)


n = 365
flip_bit(n)
