def sort(strings):
    result = []
    anagrams = {}
    for i in range(len(strings)):
        word = "".join(sorted(strings[i].lower()))
        if not word in anagrams:
            anagrams.setdefault(word, [])
        anagrams[word].append(strings[i])

    for value in anagrams.values():
        result.extend(value)

    print(result)


strings = [''] * 8
strings[0] = "abed"
strings[1] = "later"
strings[2] = "bead"
strings[3] = "alert"
strings[4] = "altered"
strings[5] = "bade"
strings[6] = "alter"
strings[7] = "alerted"

sort(strings)
