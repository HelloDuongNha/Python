from string import punctuation


def remove_punctuation(s):
    """Return copy of s with punctuation removed."""
    for c in punctuation:
        if c in s:
            s = s.replace(c, "")
    return s


from string import whitespace


def remove_whitespace(s):
    """Return copy of s with whitespace removed."""
    for c in whitespace:
        if c in s:
            s = s.replace(c, "")
    return s


string = "Hello, world!! How are you doing today?"

print(string)
print(remove_punctuation(string))
print(remove_whitespace(string))
print(remove_punctuation(remove_whitespace(string)))

print()
input("Press return to continue ...")
