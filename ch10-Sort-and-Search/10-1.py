def merge(a, b, last_a, last_b):
    index_a = last_a - 1
    index_b = last_b - 1
    merged_index = last_a + last_b - 1

    while index_b > 0:
        if b[index_b] < a[index_a]:
            a[merged_index] = a[index_a]
            index_a -= 1
        else:
            a[merged_index] = b[index_b]
            index_b -= 1
        merged_index -= 1


a = [1, 3, 5, 8, None, None, None, None, None, None]
b = [2, 4, 7, 9]
last_a = len([i for i in a if i is not None])
last_b = len([i for i in b if i is not None])

merge(a, b, last_a, last_b)
print(a)
