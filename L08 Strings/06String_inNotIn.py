s1 = "Hello"
s2 = "World"

print(f"s1: {s1}")
print(f"s2: {s2}")
print()
if "He" in s1:
    print(f"'He' is a substring of '{s1}'")
else:
    print(f"'He' is not a substring of '{s1}'")

if "He" not in s2:
    print(f"'He' is not a substring of '{s2}'")
else:
    print(f"'He' is a substring of '{s2}'")

if "wor" in s2:
    print(f"'wor' is a substring of '{s2}'")
else:
    print(f"'wor' is not a substring of '{s2}'")

print()
input("Press return to continue ...")
