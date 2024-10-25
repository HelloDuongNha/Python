import urllib.request


def letter_frequency(s):
    """ Count each letter in the string """
    counts = 26 * [0]  # Create and initialize counts
    for ch in s:
        if ch.isalpha():
            counts[ord(ch) - ord("a")] += 1
    return counts


url = "https://www.gre.ac.uk/"
# url = input("Enter an URL for a file: ").strip()
infile = urllib.request.urlopen(url)
content = infile.read().decode() # Read the content as string

counts = letter_frequency(content.lower())

for i in range(len(counts)):
    if counts[i] != 0:
        print(f"{chr(ord('a') + i)} appears {counts[i]:5} times")

print()
input("Press return to continue ...")
