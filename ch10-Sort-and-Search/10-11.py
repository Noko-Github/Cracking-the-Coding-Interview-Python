import sys


def sort_valley_peak(array):
    for i in range(1, len(array), 2):
        biggest_index = max_index(array, i-1, i, i+1)
        swap(array, i, biggest_index)

    return array


def max_index(array, a, b, c):
    array_len = len(array)
    a_value = array[a] if a > 0 and array_len > a else -sys.maxsize
    b_value = array[b] if b > 0 and array_len > b else -sys.maxsize
    c_value = array[c] if c > 0 and array_len > c else -sys.maxsize

    max_value = max([a_value, b_value, c_value])
    if a_value == max_value:
        return a
    if b_value == max_value:
        return b
    if c_value == max_value:
        return c


def swap(array, left, right):
    temp = array[left]
    array[left] = array[right]
    array[right] = temp


array = [9, 1, 0, 4, 8, 7]
print(sort_valley_peak(array))
