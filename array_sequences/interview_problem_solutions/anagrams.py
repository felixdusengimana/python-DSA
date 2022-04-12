def anagram_with_built_in_methods(s1: str, s2: str):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    return sorted(s1) == sorted(s2)


def anagram_without_built_in_methods(s1: str, s2: str):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # Edge case check.
    if len(s1) != len(s2):
        return False

    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True


print(anagram_without_built_in_methods("namess", "anamss"))