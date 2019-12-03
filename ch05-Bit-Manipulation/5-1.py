def update_bits(n, m, i, j):

    m_shifted = m << i
    right_mast = (1 << i) - 1
    left_mask = -1 << j + 1
    mask = left_mask | right_mast
    n_cleared = n & mask

    return n_cleared | m_shifted


n = 0b10000000000
m = 0b10011
i = 2
j = 6

print(bin(update_bits(n, m, 0, 2)))
