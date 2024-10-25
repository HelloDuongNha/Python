def print_list(items, header=None):
    if header != None:
        print(header)
    for item in items:
        print(f"{item}")
    print()


letters = ["a", "b", "c", "d", "e", "f", "g"]

print("VALUES")
print("letters[1] = " + letters[1])
print("letters[-1] = " + letters[-1])
print("letters[-2] = " + letters[-2])
print("letters[-3] = " + letters[-3])
#print("letters[-10] = " + letters[-10]) # will produce an error
print()

print("SLICES")
print_list(letters, "letters")
print_list(letters[:1], "letters[:1]")
print_list(letters[1:], "letters[1:]")
print_list(letters[:-1], "letters[:-1]")
print_list(letters[-1:], "letters[-1:]")
print_list(letters[2:4], "letters[2:4]")
print_list(letters[5:100], "letters[5:100]")
print_list(letters[::2], "letters[::2]")
print_list(letters[1::2], "letters[1::2]")
print_list(letters[::-1], "letters[::-1]")

print()
input("Press return to continue ...")
