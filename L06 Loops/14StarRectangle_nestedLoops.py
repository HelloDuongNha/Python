rows = int(input("How many rows? "))
cols = int(input("How many columns? "))
for row in range(rows):
    output = ""
    for col in range(cols):
        output += "*"
    print(output)

print()
input("Press return to continue ...")
