def is_permutation_of_palindorome(phrase):
    array = [0]*256
    phrase = phrase.replace(' ', '')
    for char in phrase:
        index = ord(char)
        array[index] = 1 if array[index] == 0 else 0

    print(sum(array))
    return sum(array) == 0 if len(phrase) % 2 == 0 else sum(array) == 1


string = 'tact coa'
print(is_permutation_of_palindorome(string))
