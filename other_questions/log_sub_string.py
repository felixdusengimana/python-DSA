def return_substring(str, word):
    left_str = str
    substring = True
    for letter in word:
        if letter in left_str:
            _index = left_str.find(letter)
            left_str = left_str[_index + 1:]
        else:
            substring = False

    return substring


def calculate_long_sub_str(str, words):
    long_sub_words = ""
    for word in words:
        if return_substring(str, word):
            len(long_sub_words)
            if len(long_sub_words) < len(word):
                long_sub_words = word

    return long_sub_words


str = "abppplee"
words = {"able", "ale", "apple", "bale", "kangaroo"}
print(calculate_long_sub_str(str, words))
