def swap_odd_even_bit(value):
    return (value & 0xaaaaaaaa >> 1) | (value & 0x55555555 << 1)


value = 100
print(swap_odd_even_bit(value))
