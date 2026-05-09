about = 6 - 7
about, face = 6, about * 7


def make_something(f):
    if f(about):
        f = lambda k: about

    def something(about):
        return print(f(about) or print(about))

    return something


f = lambda x: 10 * x

# (a)
# -7
# None
print(print(face))

# (b)
# 6
# 8
# 8
# None