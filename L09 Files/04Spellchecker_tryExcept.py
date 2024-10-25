def read(filename):
    """Return contents of text file as string."""
    with open(filename) as file:
        return file.read()


try:
    valid_words = read("dictionary.txt").split()
    print("spellchecking ...")
    while True:
        word = input("Enter a word (or hit return to cancel): ")
        if len(word) == 0:
            break
        if word.lower() in valid_words:
            print(f" '{word}' looks ok")
        else:
            print(f" '{word}' not in this dictionary")
    print("spellchecking ... finished")
except OSError as err:
    print(err)
    print("Stopping, unable to read dictionary file.")

print()
input("Press return to continue ...")
