s1 = "Hello"
s2 = "World"

print(f"s1: {s1}")
print(f"s2: {s2}")
print()
print("SLICES")
print(f"s1[1:3]: {s1[1:3]}")
print(f" s1[3:]: {s1[3:]}")
print(f" s1[:2]: {s1[:2]}")
print()
print("ADD & MULTIPLY")
print(f"s1 + s2: {s1 + s2}")
print(f" 2 * s1: {(2 * s1)}")
print()
print("ADD & MULTIPLY ASSIGNMENT")
s1 += s2
print(f"s1 += s2; s1: {s1}")
s2 *= 3
print(f"s2 *= 3;  s2: {s2}")
print()

print()
input("Press return to continue ...")
