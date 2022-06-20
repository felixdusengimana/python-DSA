# Given a fibonacci number return the previous fibonacci or -1 if the number is't  fibonacci
import math


def is_perfect_square(n):
    s = int(math.sqrt(n))
    return s*s == n


def prev_fibonacci(n: int):
    if is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4):
        a = n / ((1 + math.sqrt(5)) / 2.0)
        return round(a)
    else:
        return -1


print(prev_fibonacci(233))
