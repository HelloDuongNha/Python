import urllib.request


def frequency(items):
    """Return count of each item in list of items."""
    count = {}
    for item in items:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    return count


url = "https://www.gre.ac.uk/"
# url = input("Enter an URL for a file: ").strip()
infile = urllib.request.urlopen(url)
content = infile.read().decode() # Read the content as string

count = frequency(content.lower())

print("CHARACTER FREQUENCY - sorted by character")
sorted_keys = sorted(count)
for key in sorted_keys:
    if key.isalpha():
        print(f"{count.get(key):5} {key}")

print()
input("Press return to continue ...")
