import os


def read(filename):
    """Return contents of text file as a string."""
    with open(filename) as file:
        return file.read()


try:
    file = open("demo.txt", "w")
    file.write("Hello world!\n")
    file.close()

    print("demo.txt:")
    print(read("demo.txt"))

    input("Press return to continue ...")
    print()

    file = open("demo.txt", "a")
    file.write("Hello again!\n")
    file.close()

    print("demo.txt:")
    print(read("demo.txt"))

    input("Press return to continue ...")
    print()

    print("deleting demo.txt")
    os.remove("demo.txt")

except OSError as err:
    print(err)
    print("Stopping, can't access demo.txt.")

print()
input("Press return to continue ...")
