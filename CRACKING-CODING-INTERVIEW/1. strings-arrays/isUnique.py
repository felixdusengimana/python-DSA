# Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

# Work through
#
#  2. add element in hashtable at each string iteration
#  3. if we found our character in hash table return false
#  4. if we end our string iterating without any duplicates return true

def isUnique(word: str):
    if len(word) <= 1:
        return True
    if len(word) > 128:
        return False
    # 1. create a hash table
    char_hashtable = {}
    # 2. loop through string
    for char in word:
        # 3. add element in hashtable at each string iteration
        if char_hashtable.get(char):
            return False
        else:
            char_hashtable[char] = 1
    print(char_hashtable)
    return True


print(isUnique("Hii"))
