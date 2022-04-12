def sentence_reversal(text: str):
    arrwords = text.strip().split(" ")

    return " ".join(reversed(arrwords))


def reversal(text: str):
    words = []
    spaces = [' ']
    length = len(text)
    i = 0

    while i < length:
        if text[i] not in spaces:
            word_start = i

        while i < length and text[i] not in spaces:
            i += 1
        words.append(text[word_start:i])

        i += 1

    return " ".join(reversed(words))


print(sentence_reversal("this is the best"))
print(reversal("this is the best"))