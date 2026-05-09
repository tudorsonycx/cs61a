def hailstone(n):
    """Print numbered updates in the hailstone sequence.
    >>> hailstone(10)
    1 10 -> 5
    2 5 -> 16
    3 16 -> 8
    4 8 -> 4
    5 4 -> 2
    6 2 -> 1
    """

    def f():
        if n % 2 == 1:
            m = 3 * n + 1
        else:
            m = n // 2

        print(k, n, '->', m)

        return m


    k = 1
    while n > 1:
        k, n = k + 1, f()
