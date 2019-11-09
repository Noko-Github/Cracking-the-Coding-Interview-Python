def one_edit_away(s1, s2):
    if len(s1) == len(s2):
        return one_edit_away(s1, s2)
    else:
        return one_edit_insert(s1, s2)

    return False


def one_edit_replace(s1, s2):
    did_found_diff = False
    for char1, char2 in zip(s1, s2):
        if char1 != char2:
            did_found_diff = True
            if did_found_diff:
                return False

    return True


def one_edit_insert(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    else:
        longer = s1 if len(s1) > len(s2) else s2
        shorter = s1 if len(s1) < len(s2) else s2
        runner_longer = 0
        runner_shorter = 0
        did_found_diff = False
        while runner_shorter < len(shorter):
            print(runner_shorter)
            if longer[runner_longer] != shorter[runner_shorter]:
                if did_found_diff:
                    return False
                else:
                    did_found_diff = True
                runner_longer += 1
            else:
                runner_shorter += 1
                runner_longer += 1

        return True


s1 = 'pale'
s2 = 'pal'
print(one_edit_away(s1, s2))
