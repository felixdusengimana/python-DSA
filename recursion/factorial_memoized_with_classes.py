class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.f(*args)

        return self.memo[args]


def factorial(n):
    if n < 2:
        return 1
    return factorial(n - 1) * n


factorial_a = Memoize(factorial)

print(factorial_a(5))
print(factorial_a(10))
