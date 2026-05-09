def fifty_evens(t):
    "The next function for the finite sequence of the first 50 positive even numbers."
    if t % 2 == 0 and t < 100:
        return t + 2
    return 0


def next_square(t):
    """Compute the next perfect square.
    >>> next_square(0)
    1
    >>> next_square(16)
    25
    >>> next_square(17) # Not a perfect square
    0
    """

    sqrt_t = t ** 0.5

    if int(sqrt_t) != sqrt_t:
        return 0

    return int((sqrt_t + 1) ** 2)


def sum_sequence(f):
    """Return the sum of terms in a finite sequence.
    >>> sum_sequence(fifty_evens) # 2 + 4 + 6 + 8 + ... + 98 + 100 = 2550
    2550
    """
    t = f(0)
    s = t

    while t:
        t = f(t)
        s += t

    return s


def cap(f, n):
    """Return the next function for the up-sequence for f up to (and possibly including) n.
    >>> squares_up_to_25 = cap(next_square, 30) # 30 is not in the next_square sequence
    >>> squares_up_to_25(4)
    9
    >>> squares_up_to_25(16)
    25
    >>> squares_up_to_25(25)
    0
    >>> squares_up_to_25(17) # 17 is not in the next_square sequence
    0
    >>> cap(next_square, 81)(64) # 81 is in the next_square sequence
    81
    """

    def capped(x):
        t = f(x)

        if t > n:
            return 0

        return t

    return capped


def max_term(f):
    """Returns the largest term in the finite up-sequence for next function f.
    >>> max_term(cap(next_square, 20)) # 16 is the largest square less than or equal to 20.
    16
    """

    t = f(0)
    res = 0

    while t:
        res = t
        t = f(t)

    return res


def reverse(f):
    """Return the previous function for the up-sequence encoded by next function f.
    >>> rev_squares = reverse(cap(next_square, 30)) # Goes in reverse through 1, 4, 9, 16, 25
    >>> print(rev_squares(0), rev_squares(25), rev_squares(16), rev_squares(9), rev_squares(4))
    25 16 9 4 1
    >>> rev_squares(1) # 1 is the first term
    0
    >>> rev_squares(10) # 10 is not in the sequence
    0
    """

    def previous(t):
        if t == 0:
            return max_term(f)

        x = t - 1
        while x > 0 and f(x) != t:
            x = x - 1

        return x

    return previous


def reverse_iter(f):
    """Return the previous function for the up-sequence encoded by next function f.
    >>> rev_squares = reverse_iter(cap(next_square, 30)) # Goes in reverse through 1, 4, 9, 16, 25
    >>> print(rev_squares(0), rev_squares(25), rev_squares(16), rev_squares(9), rev_squares(4))
    25 16 9 4 1
    >>> rev_squares(1) # 1 is the first term
    0
    >>> rev_squares(10) # 10 is not in the sequence
    0
    """

    def h(f, t, next_t):
        return lambda n: t if n == next_t else f(n)

    t = f(0)
    res = h(lambda _: 0, 0, t)

    while t:
        next_t = f(t)
        res = h(res, t, next_t)

        t = next_t

    return res


def reverse_rec(f):
    """Return the previous function for the up-sequence encoded by next function f.
    >>> rev_squares = reverse_rec(cap(next_square, 30)) # Goes in reverse through 1, 4, 9, 16, 25
    >>> print(rev_squares(0), rev_squares(25), rev_squares(16), rev_squares(9), rev_squares(4))
    25 16 9 4 1
    >>> rev_squares(1) # 1 is the first term
    0
    >>> rev_squares(10) # 10 is not in the sequence
    0
    """

    def h(t, res):
        next_t = f(t)

        if next_t == 0:
            return lambda n: t if n == 0 else res(n)

        return h(next_t, lambda n: t if n == next_t else res(n))

    return h(0, lambda n: 0)


def reverse_efficient(f):
    """Return the previous function for the up-sequence encoded by next function f.
    >>> rev_squares = reverse_efficient(cap(next_square, 30)) # Goes in reverse through 1, 4, 9, 16, 25
    >>> print(rev_squares(0), rev_squares(25), rev_squares(16), rev_squares(9), rev_squares(4))
    25 16 9 4 1
    >>> rev_squares(1) # 1 is the first term
    0
    >>> rev_squares(10) # 10 is not in the sequence
    0
    """

    t = f(0)

    d = {t: 0}

    while t:
        next_t = f(t)
        d[next_t] = t

        t = next_t

    return lambda n: d.get(n, 0)


def sum_below(f, n):
    """Return the sum of the terms of the sequence for f that are below n,
    where n is a term in the sequence for f.
    >>> sum_below(next_square, 25) # 1 + 4 + 9 + 16
    30
    """
    assert f(n), 'n is not a term of the up-sequence for f'
    return sum_sequence(lambda t: f(t) != n and f(t))
