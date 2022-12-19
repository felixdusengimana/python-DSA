# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.

# work through
#  1. check if string length are equal, if not return false
#  2. add occurrence of characters in string 1 into a hash map(dictionary)
#  3. remove each occurrence by one character in string 2
#  4. return true if our hashmap is empty
def check_permutation(string1: str, string2: str):
    if len(string1) != len(string2):
        return False
    char_dict = {}
    for char in string1:
        if char_dict.get(char):
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    for char in string2:
        if not char_dict.get(char):
            return False
        else:
            if char_dict.get(char) == 1:
                char_dict.pop(char)
            else:
                char_dict[char] -= 1

    return char_dict.__len__() == 0


print(check_permutation("a   ", '   a'))
# print(check_permutation('! !', '!@!'))
