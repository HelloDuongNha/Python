from string import punctuation
from string import whitespace


def remove_punctuation(s):
    """Return copy of s with punctuation removed."""
    for c in punctuation:
        if c in s:
            s = s.replace(c, "")
    return s


def remove_whitespace(s):
    """Return copy of s with whitespace removed."""
    for c in whitespace:
        if c in s:
            s = s.replace(c, "")
    return s


def frequency(items):
    """Return count of each item in list of items."""
    count = {}
    for item in items:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    return count


string = "Hello world!"
string = string.lower()
string = remove_punctuation(string)
string = remove_whitespace(string)

characters = list(string)

count = frequency(characters)

print("CHARACTER FREQUENCY - unordered")
for key in count:
    print(f"{count.get(key)} {key}")
print()

print("CHARACTER FREQUENCY - sorted by character")
sorted_keys = sorted(count)
for key in sorted_keys:
    print(f"{count.get(key)} {key}")
print()

print("CHARACTER FREQUENCY - sorted by decreasing frequency")
sorted_keys = sorted(count, key=count.get)
sorted_keys.reverse()
for key in sorted_keys:
    print(f"{count.get(key)} {key}")
print()

print()
input("Press return to continue ...")
