# Displaying number pattern
#         1
#     1       1
# 1       2       1

def display_pattern(row: int):
    for i in range(1, row + 1):
        for space in range(1, (row - i) + 1):
            print(end="  ")

        C = 1
        for j in range(1, i + 1):
            print(C, ' ', sep='  ', end='')
            C = round(C * (i - j) / j)
        print()


display_pattern(12)
