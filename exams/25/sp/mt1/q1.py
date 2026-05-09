def double(x):
    return 2 * x


def square(f):
    return lambda x: f(x) * f(x)


def inc(f):
    return lambda x: f(x + 1)


def triple(f):
    return lambda x: f(f(f(x)))


def put(x):
    return lambda f: f(x)


one = put(1)
triple(print)(5)

# (a)
# 5
# None
# None

# (b)
# 4

# (c)
# 16

# (d)
old_print = print
print = (lambda p: lambda x: inc(p)(double(x)))(print)
print(100)
# or
f, print = old_print, lambda x: inc(f)(double(x))
print(100)
