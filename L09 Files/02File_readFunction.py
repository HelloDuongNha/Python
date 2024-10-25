def read(filename):
    """Return contents of text file as string."""
    with open(filename) as file:
        return file.read()


contents = read("lorem.txt")

print(contents)

words = contents.split()
for word in words:
    print(word)

print()
input("Press return to continue ...")
