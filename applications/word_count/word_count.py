import re


def word_count(s):
    counts = {}

    stripped = re.sub(r'[^\w\d\s\']+', '', s)
    for c in stripped.split():
        c = c.lower()
        if c in counts:
            counts[c] += 1

        else:
            counts[c] = 1

    return counts


# Regex explaienr:
# [^] matches everything but what is inside block quotes
# \w matches any word character
# \d matches any digit
# \s matches any whitespace
# \' matches the character '
# +  matches between one and unlimited times, as many times as possible, giving back as needed
# https://regex101.com/r/iAeuqB/13

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
