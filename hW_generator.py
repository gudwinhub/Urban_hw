str = [1, 2, 3]


def сonsequence(str):
    lenstr = len(str)

    for k in range(lenstr - 1):
        for i in range(lenstr):
            if (i + 1 + k) > lenstr:
                break
            else:
                yield str[i:i + 1 + k]
    yield str


for substr in сonsequence('abcde'):
    print(substr)
