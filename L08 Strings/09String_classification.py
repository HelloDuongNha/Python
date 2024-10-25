string = "COMP1753"

if string.isalnum():
    print(f"{string} is alpha-numeric (letters or numbers)")
else:
    print(f"{string} is not alpha-numeric (letters or numbers)")

if string.isalpha():
    print(f"{string} is alphabetic (just letters)")
else:
    print(f"{string} is not alphabetic (just letters)")

if string.isspace():
    print(f"{string} is whitespace")
else:
    print(f"{string} is not whitespace")

if string[:4].isalpha():
    print(string[:4] + " is alphabetic (just letters)")
else:
    print(string[:4] + " is not alphabetic (just letters)")

if string[4:].isdigit():
    print(f"{string[4:]} is numeric (just digits)")
else:
    print(f"{string[4:]} is not numeric (just digits)")

if string[:4].isupper():
    print(f"{string[:4]} is upper case")
else:
    print(f"{string[:4]} is not upper case")

if string[:4].islower():
    print(f"{string[:4]} is lower case")
else:
    print(f"{string[:4]} is not lower case")

if string[4:].islower():
    print(f"{string[4:]} is lower case")
else:
    print(f"{string[4:]} is not lower case")

print()
input("Press return to continue ...")
