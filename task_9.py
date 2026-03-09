def memoize(func):
    """Decorator for caching results"""
    cache = {}

    def wrapper(n):
        if n in cache:
            return cache[n]

        result = func(n)
        cache[n] = result
        return result

    return wrapper


@memoize
def factorial(n):
    """Calculates factorial"""
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(5))
print(factorial(5))
