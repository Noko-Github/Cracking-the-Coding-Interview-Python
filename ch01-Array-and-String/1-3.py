def replace_spaces(string, true_length):
    replaced_length = 0
    reader = len(string) - 1
    for s in string:
        if s == ' ':
            replaced_length += 3
        else:
            replaced_length += 1

    string += [' '] * (replaced_length - len(string))
    writer = len(string) - 1
    while reader >= 0 and writer >= 0:
        if string[reader] == ' ':
            string[writer] = '0'
            string[writer-1] = '2'
            string[writer-2] = '%'
            reader -= 1
            writer -= 3
        else:
            string[writer] = string[reader]
            reader -= 1
            writer -= 1

    return string


string = 'Mr John Smith '
replaced = replace_spaces(list(string), 13)
print(replaced)
