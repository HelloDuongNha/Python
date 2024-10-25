response = input("Are you generally happy with COMP1753? ")

# with chaining
if response.strip().lower().startswith("yes"):
    print(f"Good! Your response is '{response}'")

# without chaining
response = response.strip()
response = response.lower()
if response.startswith("yes"):
    print(f"Good! Your response is '{response}'")

print()
input("Press return to continue ...")
