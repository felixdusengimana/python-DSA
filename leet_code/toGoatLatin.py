class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        VOWELS = ['a', 'e', 'i', 'o', 'u']

        splitted_words = sentence.split(" ")
        sent = []
        for idx, word in enumerate(splitted_words):
            if word[0] in VOWELS:
                word += 'ma' + ('a' * (idx + 1))
            else:
                first_char = word[0]
                word = word[1::] + first_char + 'ma' + ('a' * (idx + 1))
            sent.append(word)

        return " ".join(sent)


sol = Solution()
print(sol.toGoatLatin("I speak Goat Latin"))
