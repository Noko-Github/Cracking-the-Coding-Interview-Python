def search(array, target, first, last):
    if first > last:
        return None

    mid_index = (first + last)/2
    if array[mid_index] == target:
        return mid_index
    elif array[mid_index] == "":
        left = mid_index - 1
        right = mid_index + 1
        while True:
            if left < first and last < right:
                return None
            elif right < last and array[right] != '':
                mid_index = right
                break
            elif first < left and array[left] != '':
                mid_index = left
                break
            left -= 1
            right += 1

    if array[mid_index] < target:
        return search(array, target, mid_index+1, last)
    else:
        return search(array, target, first, mid_index-1)


array = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
target = "ball"

print(search(array, target, 0, len(array) - 1))
