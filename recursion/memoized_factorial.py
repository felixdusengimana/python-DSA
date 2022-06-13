factorial_cashes = {}


def factorial(n):
    if n < 2:
        return 1
    elif n in factorial_cashes:
        return factorial_cashes[n]
    else:
        x = factorial(n - 1) * n
        factorial_cashes[n] = x
        return x


print(factorial(5))
print(factorial(2))
