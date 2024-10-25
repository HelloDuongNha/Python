string = "Hello world!"
print(string)
print()

# print each character on a new line
for c in string:
    print(c)
print()

# print each character separated by a space
for c in string:
    print(c, end=" ")
print()
print()

# print each character unseparated
#  effectively just print out the string
for c in string:
    print(c, end="")
print()
print()

# print each character separated by a *
for c in string:
    print(c, end="*")
print()
print()

# print every other character separated by a *
for c in string[::2]:
    print(c, end="*")
print()
print()

print()
input("Press return to continue ...")
