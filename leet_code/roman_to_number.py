def roman_to_number(s):
    ROMAN_LETTERS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    split_letter = list(s)
    number = ROMAN_LETTERS[split_letter[0]]
    idx = 0

    while idx < len(split_letter):
        ROMAN_LETTERS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        i = 0
        num = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i + 1] in ROMAN_LETTERS:
                if ROMAN_LETTERS[s[i+1]] > ROMAN_LETTERS[s[i]]:
                    num += ROMAN_LETTERS[s[i+1]] - ROMAN_LETTERS[s[i]]
                    i += 2
                else:
                    num += ROMAN_LETTERS[s[i]]
                    i += 1
            else:
                num += ROMAN_LETTERS[s[i]]
                i += 1
        return num


print(roman_to_number("IV"))
