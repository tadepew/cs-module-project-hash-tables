import re


def no_dups(s):
    counts = {}
    res = ""

    words = s.split()

    for c in words:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
            res += str(c + ' ')

    return res.strip()


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
