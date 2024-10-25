size = int(input("What size triangle? "))
for row in range(size):
    output = ""
    for col in range(row+1):
        output += "*"
    print(output)

print()
input("Press return to continue ...")
