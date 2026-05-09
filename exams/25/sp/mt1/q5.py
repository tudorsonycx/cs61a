def at_least_two(x, y, z):
    """Returns whether at least two of the arguments are true values.
    >>> at_least_two(1 + 1, 3 + 3, 5 + 5)
    True
    >>> at_least_two(1 + 1, 3 - 3, 5 + 5)
    True
    >>> at_least_two(1 - 1, 3 + 3, 5 + 5)
    True
    >>> at_least_two(1 - 1, 3 + 3, 0)
    False
    >>> at_least_two(1 - 1, 0, 0)
    False
    """
    if x:
        return bool(y or z)

    return bool(y and z)
