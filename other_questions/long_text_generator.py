vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def long_text_generator(text, times):
    long_text = ""
    for e in text:
        if e in vowels:
            long_text = "".join([long_text, e * times])
        else:
            long_text = "".join([long_text, e])

    return long_text


print(long_text_generator('ANo', 2))
