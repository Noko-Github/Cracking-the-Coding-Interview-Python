def search(array, left, right, x):
    mid_index = (left + right) / 2
    mid_value = array[mid_index]
    if left > right:
        return None

    if mid_value == x:
        return mid_index

    if array[mid_index] < array[right]:
        if x > array[mid_index] and array[right] > x:
            return search(array, mid_index+1, right, x)
        else:
            return search(array, left, mid_index-1, x)
    elif array[mid_index] > array[left]:
        if x < array[mid_index] and array[left] < x:
            return search(array, left, mid_index-1, x)
        else:
            return search(array, mid_index+1, right, x)
    elif array[left] == array[mid_index]:
        pass


array = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
search(array, array[0], array[-1], 7)
