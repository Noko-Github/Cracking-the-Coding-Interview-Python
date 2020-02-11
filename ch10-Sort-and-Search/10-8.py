class BitSet:

    def __init__(self, size):
        self.bitset = [0] * ((size >> 5)+1)
        print(len(self.bitset))

    def get(self, pos):
        word_number = (pos >> 5)
        bit_number = (pos & 0x1f)
        return (self.bitset[word_number] & (1 << bit_number)) != 0

    def set(self, pos):
        word_number = (pos >> 5)
        bit_number = (pos & 0x1f)
        self.bitset[word_number] |= 1 << bit_number


def check_duplicates(array):
    bit = BitSet(32000)
    duplicate_values = []
    for pos in range(len(array)):
        number = array[pos]
        num0 = number - 1
        if bit.get(num0):
            duplicate_values.append(number)
        else:
            bit.set(num0)

    return duplicate_values


array = [1, 2, 3, 4, 4, 5, 5, 6, 7, 8, 8, 9]
print(check_duplicates(array))
