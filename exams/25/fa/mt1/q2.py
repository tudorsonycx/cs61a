def use(silk):
    a = 2
    print(lace(silk), a)

def lace(pin):
    a = print(pin())
    return a

a = 1
thread = lambda x: a + x
a = 3
needle = lambda: thread(a * 10)

use(needle)
print(a)

# (a)
# None 2
# (b)
# 33
# (c)
# 3
