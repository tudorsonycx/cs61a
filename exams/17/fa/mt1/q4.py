def collapse(n):
    """For non-negative N, the result of removing all digits that are equal
    to the digit on their right, so that no adjacent digits are the same.
    >>> collapse(1234)
    1234
    >>> collapse(12234441)
    12341
    >>> collapse(0)
    0
    >>> collapse(3)
    3
    >>> collapse(11200000013333)
    12013
    """
    if n > 0:
        if n % 10 == n // 10 % 10:
            return collapse(n // 10)
        else:
            return collapse(n // 10) * 10 + n % 10

    return n


def collapse_tailrec(n):
    """
    >>> collapse_tailrec(1234)
    1234
    >>> collapse_tailrec(12234441)
    12341
    >>> collapse_tailrec(0)
    0
    >>> collapse_tailrec(3)
    3
    >>> collapse_tailrec(11200000013333)
    12013
    """

    def loop(n, res, p):
        if n == 0:
            return res
        if n % 10 == n // 10 % 10:
            return loop(n // 10, res, p)
        return loop(n // 10, n % 10 * 10 ** p + res, p + 1)

    return loop(n, 0, 0)


def find_pair(p):
    """Given a two-argument function P, return a function that takes a
    non-negative integer and returns True if and only if two adjacent digits
    in that integer satisfy P (that is, cause P to return a true value).
    >>> z = find_pair(lambda a, b: a == b) # Adjacent equal digits
    >>> z(1313)
    False
    >>> z(12334)
    True
    >>> z = find_pair(lambda a, b: a > b)
    >>> z(1234)
    False
    >>> z(123412)
    True
    >>> find_pair(lambda a, b: a <= b)(9753)
    False
    >>> find_pair(lambda a, b: a == 1)(1) # Only one digit; no pairs.
    False
    """

    def find(n):
        while n >= 10:
            if p(n // 10 % 10, n % 10):
                return True

            n //= 10

        return False

    return find


def find_pair_rec(p):
    """Given a two-argument function P, return a function that takes a
    non-negative integer and returns True if and only if two adjacent digits
    in that integer satisfy P (that is, cause P to return a true value).
    >>> z = find_pair_rec(lambda a, b: a == b) # Adjacent equal digits
    >>> z(1313)
    False
    >>> z(12334)
    True
    >>> z = find_pair_rec(lambda a, b: a > b)
    >>> z(1234)
    False
    >>> z(123412)
    True
    >>> find_pair_rec(lambda a, b: a <= b)(9753)
    False
    >>> find_pair_rec(lambda a, b: a == 1)(1) # Only one digit; no pairs.
    False
    """

    def find(n):
        if n >= 10:
            if p(n // 10 % 10, n % 10):
                return True

            return find(n // 10)

        return False

    return find
