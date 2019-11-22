def search(array, x):
    k = 1
    while array.elementAt(k) != -1 and array[k] < x:
        k *= 2

    return binary_search(array, 0, k, x)


def binary_search(array, left, right, x):
    mid_index = (left + right)/2
    if array[mid_index] == x:
        return mid_index

    if array[mid_index] < x or array[mid_index] == -1:
        return binary_search(array, mid_index+1, right, x)
    else:
        return binary_search(array, left, mid_index-1, x)


array = [1, 2, 5, 7, 9, 10, 11, 45, 66, 78, 91, 199, 201]
index = search(array, x)
