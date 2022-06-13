cashes = {}


def fib_series(n):
    if n < 1:
        return n

    if n in cashes:
        return cashes[n]
    else:
        fib = fib_series((n - 1)) + n
        cashes[n] = fib
        return fib


print(fib_series(10))
