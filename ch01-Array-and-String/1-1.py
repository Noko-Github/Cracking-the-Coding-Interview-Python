def is_unique_chars(str):
    array = [0] * 256

    for char in str:
        ascii_index = ord(char)
        if array[ascii_index] == 1:
            return False
        else:
            array[ascii_index] = 1

    return True


str = 'abcdef'
print(is_unique_chars(str))
