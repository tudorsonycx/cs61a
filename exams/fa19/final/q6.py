def pal(n):
    """Return a palindrome starting with n.
    >>> pal(12430)
    1243003421
    """
    m = n

    while m > 0:
        n = n * 10 + m % 10
        m //= 10

    return n


def contains(a, b):
    """Return whether the digits of a are contained in the digits of b.
    >>> contains(357, 12345678)
    True
    >>> contains(753, 12345678)
    False
    >>> contains(357, 37)
    False
    """
    if a == b:
        return True

    if a > b:
        return False

    if a % 10 == b % 10:
        return contains(a // 10, b // 10)

    return contains(a, b // 10)


def contains_alt(a, b):
    """Return whether the digits of a are contained in the digits of b.
    >>> contains_alt(357, 12345678)
    True
    >>> contains_alt(753, 12345678)
    False
    >>> contains_alt(357, 37)
    False
    """
    if a == 0:
        return True

    if a > b:
        return False

    if a % 10 == b % 10:
        return contains_alt(a // 10, b // 10)

    return contains_alt(a, b // 10)


def biggest_palindrome(n):
    """Return the largest even-length palindrome in n.
    3425534
    4355243
    >>> biggest_palindrome(3425534)
    4554
    >>> biggest_palindrome(126130450234125)
    21300312
    """
    m = n
    rev = 0
    while m > 0:
        rev = rev * 10 + m % 10
        m //= 10

    def loop(x, y):
        if x == 0 or y == 0:
            return 0

        if x % 10 == y % 10:
            return loop(x // 10, y // 10) * 10 + x % 10
        else:
            p1 = loop(x // 10, y)
            p2 = loop(x, y // 10)
            return max(p1, p2)

    return loop(n, rev)


def palinkdrome(n):
    return outer([], n)


def outer(r, n):
    def f(k):
        t = r + [k]

        if n == 1:
            s = t[:]

            while t:
                s.append(t[-1])

                t.pop()

            return s
        return outer(t, n - 1)

    return f
