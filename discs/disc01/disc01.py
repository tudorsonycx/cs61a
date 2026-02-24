def race(x, y):
    """The tortoise always walks x feet per minute, while the hare repeatedly
    runs y feet per minute for 5 minutes, then rests for 5 minutes. Return how
    many minutes pass until the tortoise first catches up to the hare.

    >>> race(5, 7)  # After 7 minutes, both have gone 35 steps
    7
    >>> race(2, 4) # After 10 minutes, both have gone 20 steps
    10
    >>> race(2, 3) # Normally should return 8, but while continuation condition is erroneous
    15
    """

    assert x < y <= 2 * x, 'the hare must be fast but not too fast'
    tortoise, hare, minutes = 0, 0, 0
    # the tortoise - hare condition is incorrect; even if tortoise becomes larger
    # than hare at any point, which means that the tortoise has overtaken the hare,
    # the while loop will continue for yet another iteration, only stopping when,
    # and if, tortoise becomes exactly equal to hare.
    while minutes == 0 or tortoise - hare:
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
    return minutes


def race_fixed(x, y):
    """Fixed version of race, with correct loop continuation condition.
    This function will actually only return a value from the following set of 5
    possible values: {6, 7, 8, 9, 10}, and it will never enter an infinite loop,
    as long as y is less than or equal, at most, to 2 * x. The "trick" to this
    conclusion is to realize that the only moments the tortoise can catch up to
    the hare is within the first 5 minutes in which the hare is resting. That's it.
    x being strictly less than y evidently means that the tortoise can't possibly
    catch up during the first 5 minutes of the race. It has a chance, and
    always will manage to catch up to it during those 5 minutes that the hare
    is resting, as long as y <= 2 * x.

    Proof-ish:
    we assume y <= 2x
    remember that x < y implies tortoise = 5x < 5y = hare (which denote the
    first 5 minutes of the race), after which the hare is resting for 5 minutes,
    during which the tortoise will continue to advance at the same speed.
    It will be able to catch up either after 6 minutes, denoted by the inequality
    6x >= 5y, 7 minutes, denoted by 7x >= 5y, 8 minutes, denoted by 8x >= 5y,
    9 minutes, denoted by 9x >= 5y, or 10 minutes, finally denoted by 10x >= 5y.
    We evaluate the inequality 10x >= 5y.
    10x >= 5y, implies 2x >= y which is our initial assumption.
    We've therefore proved that the tortoise will always catch up to the hare if
    y <= 2x

    We can also prove that the tortoise will never catch up to the hare if it hasn't
    done so already after 10 minutes have passed. It is (not sure) sufficient to
    show that 10nx < 5ny, which denotes the 5th minute in the n-th 5-minute period
    of rest for the hare, n > 0.
    We assume that it hasn't caught up after 10 minutes, meaning 10x < 5y;
    10x < 5y | mutliply by n. since n > 0 then we get 10nx < 5ny, which is what
    we had to prove.

    >>> race_fixed(5, 7)
    7
    >>> race_fixed(2, 4)
    10
    >>> race_fixed(2, 3)
    8
    >>> race_fixed(120, 240)
    10
    """

    assert x < y <= x * 2, 'the hare must be fast but not too fast'
    minutes, tortoise, hare = 0, 0, 0
    while minutes == 0 or tortoise < hare:
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
    return minutes


def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """

    assert 0 < n == int(n)

    i = 1
    while i <= n:
        if not i % 3 and not i % 5:
            print("fizzbuzz")
        elif not i % 3:
            print("fizz")
        elif not i % 5:
            print("buzz")
        else:
            print(i)

        i += 1


def is_prime(n):
    """Simple primality test. Checks if n is even, and if it's not, we know that
    n can't have any even divisors, so we only need to check if n has any odd
    divisors less than or equal to its square root. The reason we only have to check
    up to and including the square root of n for divisors can be understood from
    the following observation: If a number has no divisors greater than 1 and less
    than or equal to its square root, then that number is prime.
    Let N be a composite number. Assume that none of its divisors are greater than 1
    and less than or equal to sqrt(N).
    Because N is composite, N = a * b, 1 < a <= b < N. because a, b | N, a > sqrt(N)
    and since b >= a then b > sqrt(N). It follows that a * b > sqrt(N) * sqrt(N) = N,
    but a * b = N, so it follows that N > N, which is a contradiction.
    It means that our initial assumption that N has no divisors less than or equal
    to sqrt(N) is false. Therefore, if N is composite, it has to have at least one
    divisor less than or equal to sqrt(N), and if it doesn't then N must be prime.

    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    >>> is_prime(2**31 - 1) # M31 - a Mersenne prime
    True
    """

    if n <= 1:
        return False

    if not n % 2:
        return False

    i = 3
    while i <= n // i:
        if not n % i:
            return False

        i += 2

    return True


def unique_digits(n):
    """Return the number of unique digits in positive integer n.
    Goes through each of n's digits from last to first and checks whether the rest
    of the digits to the left of the current digit are equal to the current digit.
    If yes, then current digit occurs more than one time in n, and will only contribute
    to the result when the iteration arrives at its last occurance in n, when the digits
    to the left of it are obviously not equal to it; so the result is incremented
    by 1.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """

    res = 0

    while n > 0:
        d = n % 10
        n //= 10

        if not has_digit(n, d):
            res += 1

    return res


def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """

    assert 0 <= k < 10

    while n > 0:
        if n % 10 == k:
            return True

        n //= 10

    return False


def unique_digits_alt(n):
    """Return the number of unique digits in positive integer n.
    Shitty version but only goes through n once.

    >>> unique_digits_alt(8675309) # All are unique
    7
    >>> unique_digits_alt(13173131) # 1, 3, and 7
    3
    >>> unique_digits_alt(101) # 0 and 1
    2
    """

    res = 0

    zero = 0
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0

    while n > 0:
        d = n % 10

        if d == 0:
            zero = 1
        elif d == 1:
            one = 1
        elif d == 2:
            two = 1
        elif d == 3:
            three = 1
        elif d == 4:
            four = 1
        elif d == 5:
            five = 1
        elif d == 6:
            six = 1
        elif d == 7:
            seven = 1
        elif d == 8:
            eight = 1
        elif d == 9:
            nine = 1

        n //= 10

    res += zero + one + two + three + four + five + six + seven + eight + nine

    return res
