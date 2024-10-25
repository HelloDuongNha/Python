size = int(input("What size square? "))
for row in range(size):
    output = ""
    for col in range(size):
        output += "*"
    print(output)

print()
input("Press return to continue ...")
