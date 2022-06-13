def memoize(f):
    """Return memoized function."""
    cashes = {}

    def memoized(*args):
        if args not in cashes:
            cashes[args] = f(*args)
        return cashes[args]

    return memoized


@memoize
def factorial(n):
    if n < 2:
        return 1

    return n * factorial(n - 1)


print(factorial(5))
