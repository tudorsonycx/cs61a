def parabola(x):
    """A parabola function (for testing the again function)."""
    return (x - 3) * (x - 6)


def vee(x):
    """A V-shaped function (for testing the again function)."""
    return abs(x - 2)


def again(f):
    n = 1
    while True:
        m = 0
        while m < n:
            if f(m) == f(n):
                return n
            m += 1
        n += 1


def again_optimized(f):
    seen = {f(0): 0}

    n = 1

    while True:
        if f(n) in seen:
            break

        seen[f(n)] = n
        n += 1

    return seen[f(n)], n