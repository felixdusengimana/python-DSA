def unique_character_built_in(s):
    return len(set(s)) == len(s)


print(unique_character_built_in("abcd"))


def unique_character_no_built_in(s):
    chars = set()
    for char in s:
        if char in chars:
            return False
        else:
            chars.add(char)

    return True


print(unique_character_no_built_in("abcsss"))
