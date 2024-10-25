file = open("lorem.txt")
contents = file.read()

print(contents)

words = contents.split()
for word in words:
    print(word)

print()
input("Press return to continue ...")
