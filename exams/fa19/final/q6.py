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
    n = str(n)

    def loop(i, j):
        if i >= j:
            return ''

        if n[i] == n[j]:
            return n[i] + loop(i + 1, j - 1) + n[i]

        i_first = loop(i + 1, j)
        j_first = loop(i, j - 1)

        i_first_int = int(i_first) if i_first else 0
        j_first_int = int(j_first) if j_first else 0

        return i_first if i_first_int > j_first_int else j_first

    res = loop(0, len(n) - 1)

    return int(res) if res else 0


def palinkdrome(n):
    """Return a function that returns a palindrome starting with the args of n repeated calls.
    >>> print(palinkdrome(3)(5)(6)(7))
    [5, 6, 7, 7, 6, 5]
    >>> print(palinkdrome(1)(4))
    [4, 4]
    """
    return outer(None, n)



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
