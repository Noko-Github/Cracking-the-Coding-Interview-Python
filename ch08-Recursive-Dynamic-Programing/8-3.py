def magic_fast(array, start, end):
    mid_index = int((end + start)/2)
    if end < start:
        return False

    if array[mid_index] == mid_index:
        return mid_index

    if array[mid_index] > mid_index:
        return magic_fast(array, start, mid_index-1)
    else:
        return magic_fast(array, mid_index+1, end)


array = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
print(magic_fast(array, 0, len(array)))
