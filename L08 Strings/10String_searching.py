string = "Hello world!"

if string.find("or") != -1:
    print(f"'{string}' contains 'or'")
else:
    print(f"'{string}' does not contain 'or'")

if string.startswith("He"):
    print(f"'{string}' starts with 'He'")
else:
    print(f"'{string}' does not start with 'He'")

if string.endswith("world"):
    print(f"'{string}' ends with 'world'")
else:
    print(f"'{string}' does not end with 'world'")

print(f"'{string}' contains {string.count('l')} 'l' characters")
print(f"'{string}' contains {string.count('or')} 'or' substrings")

print()
input("Press return to continue ...")
