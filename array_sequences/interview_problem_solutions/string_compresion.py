def compress(string):
    counts = {}
    compressed_word = ""
    length = len(string)
    if length == 0:
        return ""

    if length == 1:
        return string+"1"

    for letter in string:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1

    for key in counts:
        compressed_word = f"{compressed_word}{key}{counts[key]}"

    return compressed_word


print(compress("AAAABBCCc"))
