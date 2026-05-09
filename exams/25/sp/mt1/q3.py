def all_digits(n, cond):
    """Return whether cond returns true for every digit of positive n.
    >>> odd = lambda d: d % 2 == 1
    >>> all_digits(123, odd) # not all digits are odd
    False
    >>> all_digits(357, odd) # all digits are odd
    True
    """

    while n > 0:
        last = n % 10

        if not cond(last):
            return False

        n //= 10

    return True


def process(n, check):
    """A function to help implement prefix_digits."""
    while n:
        if check(n):
            return n

        n = n // 10

    return 0


def prefix_digits(n, cond):
    """Return the largest prefix of positive n for which cond returns true for every digit.
    >>> odd = lambda d: d % 2 == 1
    >>> prefix_digits(94720, odd)
    9
    >>> prefix_digits(919321, odd)
    9193
    >>> prefix_digits(2025, odd)
    0
    >>> prefix_digits(20252025, lambda d: d < 4)
    202
    >>> prefix_digits(20252025, lambda d: True)
    20252025
    """

    return process(n, lambda k: all_digits(k, cond))


def prefix_digits_reimplemented(n, cond):
    """Return the largest prefix of positive n for which cond returns true for every digit.
    >>> odd = lambda d: d % 2 == 1
    >>> prefix_digits_reimplemented(94720, odd)
    9
    >>> prefix_digits_reimplemented(919321, odd)
    9193
    >>> prefix_digits_reimplemented(2025, odd)
    0
    >>> prefix_digits_reimplemented(20252025, lambda d: d < 4)
    202
    """
    k = 0

    while n >= 10 ** k:
        if cond(n // 10 ** k % 10):
            k += 1
        else:
            n //= 10
            k = 0

    return n


def prefix_digits_reimplemented_v2(n, cond):
    """Return the largest prefix of positive n for which cond returns true for every digit.
    >>> odd = lambda d: d % 2 == 1
    >>> prefix_digits_reimplemented_v2(94720, odd)
    9
    >>> prefix_digits_reimplemented_v2(919321, odd)
    9193
    >>> prefix_digits_reimplemented_v2(2025, odd)
    0
    >>> prefix_digits_reimplemented_v2(20252025, lambda d: d < 4)
    202
    """
    p = 0
    k = 0

    while n >= 10 ** p:
        if not cond(n // 10 ** p % 10):
            k = p + 1

        p += 1
    return n // 10 ** k
