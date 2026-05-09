# (b)
# i.
def tik(tok):
    def insta(gram):
        print(f"{tok} {gram}")

    return insta

# 6
# 5 None
# 7
# None None
tik(tik(5)(print(6)))(print(7))
