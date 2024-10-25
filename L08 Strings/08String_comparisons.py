s1 = "hello"
s2 = "world"
print(f"s1 = {s1}")
print(f"s2 = {s2}")
print()

if s1 == s2:
    print("s1 equals s2")
else:
    print("s1 does not equal s2")

if s1 > s2:
    print("s1 comes after s2")
else:
    print("s1 comes before s2")

if s1 <= s2:
    print("s1 comes before, or is the same as, s2")
else:
    print("s1 comes after, or is the same as, s2")

if s1 > s2.upper():
    print("s1 comes after s2.upper()")
else:
    print("s1 comes before s2.upper()")

if s1[4:] == s2[1:2]:
    print("s1[4:] equals s2[1:2]")
else:
    print("s1[4:] does not equal s2[1:2]")

print()
input("Press return to continue ...")
