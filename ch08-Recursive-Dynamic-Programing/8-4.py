import copy


def get_subset(array):
    subsets = []
    subsets.append([])
    for value in array:
        pre_subsets = copy.deepcopy(subsets)
        for subset in pre_subsets:
            subset.append(value)
            subsets.append(subset)

    return subsets


array = [1, 2, 3]
print(get_subset(array))
